import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileSystemModel, QTreeWidgetItem, QWidget, QMenu
from PyQt5 import QtCore
from FTPClient import Ui_MainWindow
from ftplib import FTP, FTP_TLS
import os
import webbrowser
from MySQLConnection import updateAccount, selectAccount
from FTPClientSettings import Ui_settingsWindow
class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.model = QFileSystemModel()
        self.uic.inputDirPathLocal.setText("C://")
        dirPathLocal = self.uic.inputDirPathLocal.text()
        self.uic.model.setRootPath(r""+dirPathLocal)
        self.uic.loadDirPathLocal.clicked.connect(self.loadDirPathLocal)
        self.uic.folderLocal.setModel(self.uic.model)
        self.uic.folderLocal.setSortingEnabled(True)
        self.uic.folderLocal.setRootIndex(self.uic.model.index(dirPathLocal))
        self.uic.folderLocal.setAlternatingRowColors(True)
        # self.uic.folderLocal.setContextMenuPolicy(CustomContextMenu)
        self.uic.btnConnect.clicked.connect(self.connect)
        self.uic.actionExit.triggered.connect(self.main_win.close)
        self.uic.actionSettings.triggered.connect(self.openSettings)
        dataMySQL = selectAccount()
        self.uic.inputHost.setText(dataMySQL[1])
        self.uic.inputUser.setText(dataMySQL[2])
        self.uic.inputPass.setText(dataMySQL[3])
        self.uic.inputPort.setText(dataMySQL[4])
        # self.uic.actionAbout.triggered.connect(self.open_url("https://www.facebook.com/"))
        # self.uic.mainLayout.setSizeConstraint(SetFixedSize);
        # self.uic.folderServer.
    def show(self):
        self.main_win.show()
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
        
    def connect(self):
        inputHost = self.uic.inputHost.text()
        inputUser = self.uic.inputUser.text()
        inputPass = self.uic.inputPass.text()
        inputPort = self.uic.inputPort.text()
        btnConnect = self.uic.btnConnect.text()
        # ftp = FTP()
        ftp = FTP_TLS()
        try:
            self.printProcess("Connecting...")
            if inputHost=="" or inputUser == "" or inputPort == "":
                self.printError("Connection information cannot be left blank")
            else:
                inputPort = int(self.uic.inputPort.text())
                
                ftp.connect(inputHost, inputPort)
                ftp.prot_c()
                self.printStatus(ftp.getwelcome())
                if btnConnect == "Disconnect":
                    try:
                        self.printProcess("DisConnecting...")
                        ftp.quit()
                        self.printStatus("DisConnect Success.")
                        self.uic.btnConnect.setText("QuickConnect")
                        self.uic.inputDirPathServer.setText("Not connected to any server")
                    except:
                        self.printError("DisConnect Failed.")
                else:
                    try:
                        self.printProcess("Perform user authentication.")
                        ftp.login(user=inputUser, passwd=inputPass)
                        self.printStatus("User authentication successful.")
                        self.printStatus("Logged on")
                        self.uic.btnConnect.setText("Disconnect")
                        pathServer = ftp.pwd()
                        self.uic.inputDirPathServer.setText(pathServer)
                        # mkdir folder 
                        l1 = QTreeWidgetItem(["String A", "String B", "String C", "String D"])
                        self.uic.folderServer.addTopLevelItem(l1)
                        dir_list = []
                        ftp.dir(dir_list.append)
                        print(dir_list)
                        # print(ftp.list())
                    except:
                        self.printError("Incorret Host/User/Pass or Port!")
        except:
            self.printError("Connection attempt failed - Incorret Host/ Port.")
        # self.printStatus("User authentication successful.")

    #############################################################
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
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self.uic.folderServer)
        creatDirectory = contextMenu.addAction("New Folder")
        download = contextMenu.addAction("Download")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
    # Hàm load dir Path để hiển thị folder cho nười dùng
    def loadDirPathLocal(self):
        dirPathLocal = self.uic.inputDirPathLocal.text()
        self.uic.model.setRootPath(r""+dirPathLocal)
        self.uic.folderLocal.setRootIndex(self.uic.model.index(dirPathLocal))  
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