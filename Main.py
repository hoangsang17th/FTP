from ftplib import FTP, FTP_TLS
from io import StringIO
import io

from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileSystemModel, QTreeWidgetItem, QWidget, QMenu
from PyQt5 import QtCore

import sys
import os
import webbrowser
from threading import Thread
from datetime import datetime

from FTPClient import Ui_MainWindow
from Dialogs.FTPClientSettings import Ui_settingsWindow
from Dialogs.CreateDirectory import Ui_createFolderWindow
from Dialogs.CreateFile import Ui_NewFileWindow
from Dialogs.Rename import Ui_RenameFileWindow

from MySQLConnection import updateAccount, selectAccount

app_icon_path = os.path.join(os.path.dirname(__file__), 'Images')
qIcon = lambda name: QIcon(os.path.join(app_icon_path, name))
class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.model = QFileSystemModel()
        self.uic.inputDirPathLocal.setText("C://")
        self.pathLocal = "C://"
        dirPathLocal = self.uic.inputDirPathLocal.text()
        self.uic.model.setRootPath(r""+dirPathLocal)
        self.uic.loadDirPathLocal.clicked.connect(self.loadDirPathLocal)
        self.uic.folderLocal.setModel(self.uic.model)
        self.uic.folderLocal.setSortingEnabled(True)
        self.uic.folderLocal.setRootIndex(self.uic.model.index(dirPathLocal))
        self.uic.folderLocal.setAlternatingRowColors(True)
        # self.uic.folderLocal.setContextMenuPolicy(CustomContextMenu)
        self.uic.btnConnect.clicked.connect(self.connect)
        self.uic.loadDirPathServer.clicked.connect(self.loadDirPathServer)
        self.uic.actionExit.triggered.connect(self.main_win.close)
        self.uic.actionSettings.triggered.connect(self.openSettings)
        self.uic.folderServer.setAlternatingRowColors(True)
        self.uic.folderServer.itemDoubleClicked.connect(self.cdToRemoteDirectory)
        self.pathServer = "Not connected to any server"
        dataMySQL = selectAccount()
        self.uic.inputHost.setText(dataMySQL[1])
        self.uic.inputUser.setText(dataMySQL[2])
        self.uic.inputPass.setText(dataMySQL[3])
        self.uic.inputPort.setText(dataMySQL[4])
        self.ftp = FTP()
        # self.uic.folderLocal.customContextMenuRequested.connect(self.contextMenuLocal)
        
        # print(self.convert_bytes(1380408))
        # force UTF-8 encoding
        self.ftp.encoding = "utf-8"
        # self.uic.actionAbout.triggered.connect(self.open_url("https://www.facebook.com/"))
        # self.uic.mainLayout.setSizeConstraint(SetFixedSize);
        # self.uic.folderServer.
    def show(self):
        self.main_win.show()
        
    def connect(self):
        inputHost = self.uic.inputHost.text()
        inputUser = self.uic.inputUser.text()
        inputPass = self.uic.inputPass.text()
        inputPort = self.uic.inputPort.text()
        btnConnect = self.uic.btnConnect.text()
        
        # ftp = FTP_TLS()
        try:
            self.printProcess("Connecting...")
            if inputHost=="" or inputUser == "" or inputPort == "":
                self.printError("Connection information cannot be left blank")
            else:
                inputPort = int(self.uic.inputPort.text())
                
                self.ftp.connect(inputHost, inputPort)
                # ftp.prot_c()
                self.printStatus(self.ftp.getwelcome())
                if btnConnect == "Disconnect":
                    try:
                        self.printProcess("DisConnecting...")
                        self.ftp.quit()
                        self.printStatus("DisConnect Success.")
                        self.uic.btnConnect.setText("QuickConnect")
                        self.uic.folderServer.clear()
                        self.disabledComponents()
                    except:
                        self.printError("DisConnect Failed.")
                else:
                    try:
                        self.printProcess("Perform user authentication.")
                        self.ftp.login(user=inputUser, passwd=inputPass)
                        self.printStatus("User authentication successful.")
                        self.printStatus("Logged on")
                        self.uic.btnConnect.setText("Disconnect")
                        self.enabledComponents()
                    except:
                        self.printError("Incorret Host/User/Pass or Port!")
        except:
            self.printError("Connection attempt failed - Incorret Host/ Port.")
        # self.printStatus("User authentication successful.")

    #############################################################
    # Làm cái double click thì vào bên trong folder bên trong cho giống cái TreeView
    def cdToRemoteDirectory(self, item):
        if str(item.text(2)) != "Folder":
            content = "Can't open file " + str(item.text(0))
            self.printError(content)
        else:

            self.pathServer = self.pathServer+ "/" + str(item.text(0))
            self.pathServer = self.pathServer.replace("//", "/")

            # print(self.pathServer)
            self.uic.inputDirPathServer.setText(self.pathServer)
            self.loadDirPathServer()
            content = "Access '"+self.pathServer +"' successful"
            self.printStatus(content)
        

    def downloadToRemoteFileList(self):
        """
        download file and directory list from FTP Server
        """
        self.remoteWordList = []
        self.remoteDir      = {}
        self.ftp.dir('.', self.addItemToRemoteFileList)
        # self.Remote_completerModel.setStringList(self.remoteWordList)

    def addItemToRemoteFileList(self, content):
        ftype, size, date, filename = self.parseFileInfo(content)
        if content.startswith('d'):
            icon = qIcon('folder.png')
            pathname = os.path.join(self.pathServer, filename)
            pathname = pathname.replace('\\', '/')
            self.remoteDir[ pathname] = True
            self.remoteWordList.append(filename)
        else:
            icon = qIcon('file.png')
        item = QTreeWidgetItem()
        item.setIcon(0, icon)
        for n, i in enumerate((filename, size, ftype, date)):
            if n == 2:
                if i == "drwxr-xr-x":
                    i = "Folder"
                elif i == "---x--x--x":
                    i = "Application"
                else:
                    i = "File"

            if n == 1:
                if i != "0":
                    num = int(i)
                    for x in ['Byte', 'KB', 'MB', 'GB', 'TB']:
                        if num < 1024:
                            num = f"{round(num, 2)}{x}"
                            break
                        num /= 1024
                    i = str(num)
                    # i = self.convert_bytes(1380408)
            item.setText(n, i)
            # print(n, i)

        self.uic.folderServer.addTopLevelItem(item)
        if not self.uic.folderServer.currentItem():
            self.uic.folderServer.setCurrentItem(self.uic.folderServer.topLevelItem(0))
            self.uic.folderServer.setEnabled(True)
        for i in range(4):
            self.uic.folderServer.resizeColumnToContents(i)
        # self.uic.folderServer.resizeColumnToContents(1)
        # self.uic.folderServer.resizeColumnToContents(2)
        # self.uic.folderServer.resizeColumnToContents(3)

    def parseFileInfo(self, file):
        """
        parse files information "drwxr-xr-x", "2", "root", "wheel", "1024", "Nov 17 1993", "lib"
        """
        # FileMode, FilesNumber, User, Group, Size, Date, Filename
        item = [f for f in file.split(' ') if f != '']
        
        ftype, size, date, filename = (item[0],  item[4], ' '.join(item[5:8]), ' '.join(item[8:]))
        # print(ftype, size, date, filename)
        return (ftype, size, date, filename)


    # Hàm hiển thị menu các chức năng để tương tác với folder client
    def contextMenuLocal(self, point):
        menu = QMenu(self.uic.folderLocal)
        upload = menu.addAction("Upload")
        open = menu.addAction("Open this folder in File Explorer")
        menu.addSeparator()
        refresh = menu.addAction("Refresh")
        action = menu.exec_(self.uic.folderLocal.mapToGlobal(point))
        if action == upload:
            self.uploadFile()
            
        if action == open:
            try:
                os.startfile(self.pathLocal)
            except:
                error = "The system cannot find the drive specified: '"+ self.pathLocal+ "'"
                self.printError(error)
        if action == refresh:
            self.loadDirPathLocal()

    def uploadFile(self):
        item = self.uic.folderLocal.selectedIndexes()
        # print(str(item[0].data()))
        srcfile  = self.pathLocal + "/" + str(item[0].data())
        dstfile  = self.pathServer + "/" + str(item[0].data())
        dstfile  = dstfile.replace('//', '/')

        try:
            file = open(srcfile, 'rb')
            self.ftp.set_pasv(0)
            self.ftp.storbinary(cmd='STOR '+dstfile, fp=file)
            self.ftp.set_pasv(1)
            self.updateDirServer()
            self.printStatus("Upload file to server successfully!")
        except:
            self.printError("Sorry! You can't upload to server!")
    # Hàm hiển thị menu các chức năng để tương tác với folder server
    def contextMenuServer(self, point):
        menu = QMenu(self.uic.folderServer)
        download = menu.addAction("Download")
        
        menu.addSeparator()
        mkdir = menu.addAction("Create directory")
        newfile = menu.addAction("Create new file .txt")
        refresh = menu.addAction("Refresh")
        menu.addSeparator()
        remove = menu.addAction("Delete")
        rename = menu.addAction("Rename")
        
        action = menu.exec_(self.uic.folderServer.mapToGlobal(point))
        if action == refresh:
            self.updateDirServer()
            self.printStatus("Refresh successful")
        if action == download:
            self.downloadFolder()
        if action == mkdir:
            self.makeFolderServer()
        if action == newfile:
            self.makeFileServer()
        if action == remove:
            self.removeFileServer()
        if action == rename:
            self.renameFileServer()

    def renameFileServer(self):
        self.renameFile = QMainWindow()
        self.uiRenameFile = Ui_RenameFileWindow()
        self.uiRenameFile.setupUi(self.renameFile)
        self.renameFile.show()
        self.uiRenameFile.btnNext.clicked.connect(self.fRenameFileServer)
        self.uiRenameFile.btnCancel.clicked.connect(self.renameFile.close)
    def fRenameFileServer(self):
        item = self.uic.folderServer.currentItem()
        if self.uiRenameFile.inputRenameFile.text() == "":
            return self.printError("Name not null!")
        try:
            old_path = self.pathServer+ "/" +str(item.text(0))
            old_path = old_path.replace("//", "/")
            new_path = self.pathServer+ "/" +self.uiRenameFile.inputRenameFile.text()
            new_path = new_path.replace("//", "/")
            self.ftp.rename(old_path, new_path)
            self.updateDirServer()
        except:
            self.printError("Can't rename thí file!")
    
    def removeFileServer(self):
        item = self.uic.folderServer.currentItem()
        for i in range(self.uic.folderServer.topLevelItemCount()):
                if(self.uic.folderServer.topLevelItem(i) == item):
                    break
        # Ngay đây cần sửa lại
        dir = self.pathServer + "/" + str(item.text(0))
        dir = dir.replace("//", "/")
        try:
            self.ftp.delete(dir)
            self.updateDirServer()
            self.uic.folderServer.setCurrentItem(self.uic.folderServer.topLevelItem(i))
            self.printStatus("Delete file successfully!")
        except:
            try:
                self.ftp.rmd(dir)
                self.updateDirServer()
                self.uic.folderServer.setCurrentItem(self.uic.folderServer.topLevelItem(i))
                self.printStatus("Delete folder successfully!")
            except:
                self.printError("Sorry, you don't have this permission!")

    def downloadFolder(self):
        
        item     = self.uic.folderServer.currentItem()
        if item.text(2) == "Folder":
                self.printError("Now, You can't download this folder.")
        else:
                srcfile  = self.pathServer + "/"+ str(item.text(0))
                srcfile  = srcfile.replace('//', '/')
                dstfile  = self.pathLocal + "/"+ str(item.text(0))
                dstfile = dstfile.replace('//', '/')
                try:
                    def callback(data):
                        file.write(data)
                    
                    file = open(dstfile, 'wb')
                    self.ftp.set_pasv(0)
                    self.ftp.retrbinary(cmd='RETR '+srcfile, callback=callback)
                    self.printStatus("Download successful!")
                    self.ftp.set_pasv(1)
                except:
                    self.printError("You can't download this file.")

    def updateDirServer(self):
        self.uic.folderServer.clear()
        self.downloadToRemoteFileList()
    # Tạo hàm để test các nút hoặc là sự kiện 1 cách nhanh chóng
    def testPrint(self):
        print("Test Ok")
    # Hàm kích hoạt các thành phần khi kết nối thành công
    def disabledComponents(self):
        self.uic.inputDirPathServer.setReadOnly(True)
        self.uic.inputDirPathServer.setText("Not connected to any server")
        self.uic.loadDirPathServer.setEnabled(False)
        self.uic.folderServer.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.download.setEnabled(False)

    def enabledComponents(self):
        self.pathServer = self.ftp.pwd()
        self.uic.inputDirPathServer.setText(self.pathServer)
        self.uic.inputDirPathServer.setReadOnly(False)
        self.uic.loadDirPathServer.setEnabled(True)
        # Khi đã kết nối thì cho phép click right
        self.uic.folderServer.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.uic.folderServer.customContextMenuRequested.connect(self.contextMenuServer)
        self.uic.folderLocal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.uic.folderLocal.customContextMenuRequested.connect(self.contextMenuLocal)
        
        self.downloadToRemoteFileList()
    # Hàm load dir Path để hiển thị folder cho nười dùng
    def loadDirPathServer(self):
        dirPathServer = self.uic.inputDirPathServer.text()
        try:
            self.ftp.cwd(dirPathServer)
            self.uic.folderServer.clear()
            self.downloadToRemoteFileList()
            self.pathServer = dirPathServer
            
            # print(self.ftp.dir())
        except:
            content = "Can't find path named " + dirPathServer
            self.printError(content) 
    # Một số chức năng tiện ích mà chúng ta sẽ cần
    def get_size_format(n, suffix="B"):
        # Chuyển đổi byte thành định dạng tỷ lệ (e.g kb, MB, v.v.)
        for unit in ["", "K", "M", "G", "T", "P"]:
            if n < 1024:
                return f"{n:.2f}{unit}{suffix}"
            n /= 1024
            # return f"{n:.2f}{unit}{suffix}"
    
    # Tạo 1 file trên server
    
    def makeFileServer(self):
        self.createFile = QMainWindow()
        self.uiCreateFile = Ui_NewFileWindow()
        self.uiCreateFile.setupUi(self.createFile)
        self.createFile.show()
        self.uiCreateFile.btnNext.clicked.connect(self.fMakeFileServer)
        self.uiCreateFile.btnCancel.clicked.connect(self.createFile.close)
    
    def fMakeFileServer(self):
        try:
            content = "Create a file named "+ self.uiCreateFile.inputCreateFile.text() + " with path " + self.pathServer
            self.printProcess(content)
            self.ftp.set_pasv(0)
            dir = self.pathServer+"/"+self.uiCreateFile.inputCreateFile.text()
            dir = dir.replace("//", "/")

            tmp_file = os.path.join(self.pathLocal, '##tmp##.txt')
            open(tmp_file, mode='x')
            m_time = os.stat(tmp_file).st_mtime
            webbrowser.open(tmp_file)
            while os.stat(tmp_file).st_mtime == m_time:
                pass
            
            
            file = open(tmp_file, 'rb')
            self.ftp.storbinary(cmd='STOR '+dir, fp=file)
            self.printStatus("Make file successfully!")
            self.ftp.set_pasv(1)
            self.updateDirServer()
            
            self.createFile.close()
        except Exception:
            self.printError("550 Can't create directory. Permission denied or Folder already exists")

    # Tạo 1 folder trên server
    def makeFolderServer(self):
        self.createFolder = QMainWindow()
        self.uiCreateFolder = Ui_createFolderWindow()
        self.uiCreateFolder.setupUi(self.createFolder)
        self.createFolder.show()
        self.uiCreateFolder.btnOK.clicked.connect(self.fMakeFolderServer)
        self.uiCreateFolder.btnCancel.clicked.connect(self.createFolder.close)
        
    def fMakeFolderServer(self):
        try:
            content = "Create a folder named "+ self.uiCreateFolder.inputCreateDirectory.text() + " with path " + self.pathServer
            self.printProcess(content)
            dir = self.pathServer+"/"+self.uiCreateFolder.inputCreateDirectory.text()
            dir = dir.replace("//", "/")
            self.ftp.mkd(dir)
            self.printStatus("Make folder successfully!")
            self.updateDirServer()
            self.createFolder.close()
        except Exception:
            self.printError("550 Can't create directory. Permission denied or Folder already exists")
        
    # Mở phần cài đặt ứng dụng
    def openSettings(self):
        self.windowSetting = QMainWindow()
        self.uiSetting = Ui_settingsWindow()
        self.uiSetting.setupUi(self.windowSetting)
        self.windowSetting.show()
        dataMySQL = selectAccount()
        self.uiSetting.inputHostConn.setText(dataMySQL[1])
        self.uiSetting.inputUserConn.setText(dataMySQL[2])
        self.uiSetting.inputPassConn.setText(dataMySQL[3])
        self.uiSetting.inputPortConn.setText(dataMySQL[4])
        self.uiSetting.btnSave.clicked.connect(self.saveSetting)
        self.uiSetting.btnCancel.clicked.connect(self.windowSetting.close)
    # Gọi hàm để lưu thông tin trong phần cài đặt
    def saveSetting(self):
        updateMySQL = updateAccount(
            self.uiSetting.inputHostConn.text(), 
            self.uiSetting.inputUserConn.text(),
            self.uiSetting.inputPassConn.text(),
            self.uiSetting.inputPortConn.text()
        )
        if updateMySQL:
            self.printStatus("User information update successful")
            dataMySQL = selectAccount()
            self.uic.inputHost.setText(dataMySQL[1])
            self.uic.inputUser.setText(dataMySQL[2])
            self.uic.inputPass.setText(dataMySQL[3])
            self.uic.inputPort.setText(dataMySQL[4])
        else:
            self.printError("User information update failed")
    def open_url(self, url):
        # Mở link trang web
        webbrowser.open(url)
    # Hàm load dir Path để hiển thị folder cho nười dùng
    def loadDirPathLocal(self):
        self.pathLocal = self.uic.inputDirPathLocal.text()
        self.uic.model.setRootPath(r""+self.pathLocal)
        self.uic.folderLocal.setRootIndex(self.uic.model.index(self.pathLocal))
        self.printStatus("Data refresh successful")
        
    # Sử dụng để hiển thị trạng thái cho người dùng
    # Sử dụng để hiển thị lỗi với nội dung màu đỏ
    def printError(self, message):
        self.uic.textStatus.setTextColor(QColor("red"))
        self.uic.textStatus.insertPlainText("Error: "+message+"\n")
    # Thông báo trình trạng thành công
    def printStatus(self, message):
        self.uic.textStatus.setTextColor(QColor("green"))
        self.uic.textStatus.insertPlainText("Status: "+message+"\n")
    # Báo tiến trình hiện tại của chương trình
    def printProcess(self, message):
        self.uic.textStatus.setTextColor(QColor("black"))
        self.uic.textStatus.insertPlainText("Process: "+message+"\n")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())