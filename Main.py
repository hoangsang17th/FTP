import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileSystemModel, QTreeWidgetItem, QWidget, QMenu
from PyQt5 import QtCore
from FTPClient import Ui_MainWindow
from ftplib import FTP, FTP_TLS
import os
import webbrowser
from MySQLConnection import updateAccount, selectAccount
from Dialogs.FTPClientSettings import Ui_settingsWindow
from datetime import datetime
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
        self.pathServer = "Not connected to any server"
        dataMySQL = selectAccount()
        self.uic.inputHost.setText(dataMySQL[1])
        self.uic.inputUser.setText(dataMySQL[2])
        self.uic.inputPass.setText(dataMySQL[3])
        self.uic.inputPort.setText(dataMySQL[4])
        self.ftp = FTP()
        self.uic.folderLocal.customContextMenuRequested.connect(self.contextMenuLocal)
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
                        # mkdir folder 
                        # l1 = QTreeWidgetItem(["String A", "String B", "String C", "String D"])
                        # self.uic.folderServer.addTopLevelItem(l1)
                        # self.ftp.cwd("/OS")
                        # dir_list = []
                        # self.ftp.dir(dir_list.append)
                        # print(self.ftp.mlsd("/", ["Name", "Size", "Type", "Date Modified"]))
                        # print(len(dir_list))
                        # for name, facts in self.ftp.mlsd("/OS", facts=["Size", "Type", "Date Modified"]):
    
                        #     print(name);

                        #     print("////");

                        #     print(facts);
                        # try:

                        #     self.ftp.sendcmd('LIST')
                        # except ValueError:
                        #     print(ValueError)
                        # print(ftp.nlst())
                        # print(self.ftp.dir())
                    except:
                        self.printError("Incorret Host/User/Pass or Port!")
        except:
            self.printError("Connection attempt failed - Incorret Host/ Port.")
        # self.printStatus("User authentication successful.")

    #############################################################
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
        item = self.uic.folderLocal.selectedIndexes()
        menu = QMenu(self.uic.folderLocal)
        upload = menu.addAction("Upload")
        upload.setEnabled(False)
        open = menu.addAction("Open")
        menu.addSeparator()
        mkdir = menu.addAction("Create directory")
        newfile = menu.addAction("Create new file")
        refresh = menu.addAction("Refresh")
        menu.addSeparator()
        remove = menu.addAction("Delete")
        rename = menu.addAction("Rename")
        
        action = menu.exec_(self.uic.folderLocal.mapToGlobal(point))
        if action == refresh:
            self.testPrint()
        if action == open:
            # self.uic.folderLocal.itemClicked.setText()
            try:
                os.startfile(self.pathLocal)
            except:
                error = "The system cannot find the drive specified: '"+ self.pathLocal+ "'"
                self.printError(error)
    # Hàm hiển thị menu các chức năng để tương tác với folder server
    def contextMenuServer(self, point):
        item = self.uic.folderServer.currentItem()
        menu = QMenu(self.uic.folderServer)
        download = menu.addAction("Download")
        download.setEnabled(False)
        edit = menu.addAction("View/ Edit")
        menu.addSeparator()
        mkdir = menu.addAction("Create directory")
        newfile = menu.addAction("Create new file")
        refresh = menu.addAction("Refresh")
        menu.addSeparator()
        remove = menu.addAction("Delete")
        rename = menu.addAction("Rename")
        
        action = menu.exec_(self.uic.folderServer.mapToGlobal(point))
        if action == refresh:
            self.testPrint()

    
    # Tạo hàm để test các nút hoặc là sự kiện 1 cách nhanh chóng
    def testPrint(self):
        print("Test Ok")
    # Hàm kích hoạt các thành phần khi kết nối thành công
    def disabledComponents(self):
        self.uic.inputDirPathServer.setReadOnly(True)
        self.uic.inputDirPathServer.setText("Not connected to any server")
        self.uic.loadDirPathServer.setEnabled(False)
    def enabledComponents(self):
        self.pathServer = self.ftp.pwd()
        self.uic.inputDirPathServer.setText(self.pathServer)
        self.uic.inputDirPathServer.setReadOnly(False)
        self.uic.loadDirPathServer.setEnabled(True)
        # Khi đã kết nối thì cho phép click right
        self.uic.folderServer.customContextMenuRequested.connect(self.contextMenuServer)
        
        self.downloadToRemoteFileList()
    # Hàm load dir Path để hiển thị folder cho nười dùng
    def loadDirPathServer(self):
        dirPathServer = self.uic.inputDirPathServer.text()
        try:
            self.ftp.cwd(dirPathServer)
            self.uic.folderServer.clear()
            self.downloadToRemoteFileList()
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
    
    # Xóa folder, file
    def deleteDataServer(self, dataName):
        self.ftp.delete(dataName)
    # Tạo 1 folder trên server
    def makeFolderServer(self, folderName):
        self.ftp.mkd(folderName)
    
    def loadUpdateFolderServer(self):
        self.printStatus("Server data update successful")
    # Mở phần cài đặt ứng dụng
    def openSettings(self):
        self.windowSetting = QtWidgets.QMainWindow()
        self.uiSetting = Ui_settingsWindow()
        self.uiSetting.setupUi(self.windowSetting)
        self.windowSetting.show()
        dataMySQL = selectAccount()
        self.uiSetting.inputHostConn.setText(dataMySQL[1])
        self.uiSetting.inputUserConn.setText(dataMySQL[2])
        self.uiSetting.inputPassConn.setText(dataMySQL[3])
        self.uiSetting.inputPortConn.setText(dataMySQL[4])
        self.uiSetting.btnSave.clicked.connect(self.saveSetting)
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