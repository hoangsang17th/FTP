import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileSystemModel, QWidget
from PyQt5 import QtCore
from FTPClient import Ui_MainWindow
from ftplib import FTP
import os
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
        self.uic.folderLocal.setRootIndex(self.uic.model.index(dirPathLocal))
        self.uic.folderLocal.setAlternatingRowColors(True)
        self.uic.btnConnect.clicked.connect(self.connect)
        self.uic.actionExit.triggered.connect(self.main_win.close)

    def show(self):
        self.main_win.show()
    # Hàm load dir Path để hiển thị folder cho nười dùng
    def loadDirPathLocal(self):
        dirPathLocal = self.uic.inputDirPathLocal.text()
        self.uic.folderLocal.setRootIndex(self.uic.model.index(dirPathLocal))

    def connect(self):
        inputHost = self.uic.inputHost.text()
        inputUser = self.uic.inputUser.text()
        inputPass = self.uic.inputPass.text()
        inputPort = int(self.uic.inputPort.text())
        btnConnect = self.uic.btnConnect.text()
        ftp = FTP()
        try:
            self.printProcess("Connecting...")
            ftp.connect(inputHost, inputPort)
            if btnConnect == "Disconnect":
                try:
                    self.printProcess("DisConnecting...")
                    ftp.quit()
                    self.printStatus("DisConnect Success.")
                    self.uic.btnConnect.setText("QuickConnect")
                except:
                    self.printError("DisConnect Failed.")
            else:
                try:
                    self.printProcess("Perform user authentication.")
                    ftp.login(user=inputUser, passwd=inputPass)
                    self.printStatus("User authentication successful.")
                    self.printStatus(ftp.getwelcome())
                    self.uic.btnConnect.setText("Disconnect")
                except:
                    self.printError("Incorret Host/User/Pass or Port!")
        except:
            self.printError("Connection attempt failed - Incorret Host/ Port.")
        
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