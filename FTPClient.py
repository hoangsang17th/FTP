# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FTPClient.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1121, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutTop = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutTop.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayoutTop.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayoutTop.setObjectName("horizontalLayoutTop")
        self.lbHost = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbHost.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbHost.setFont(font)
        self.lbHost.setObjectName("lbHost")
        self.horizontalLayoutTop.addWidget(self.lbHost)
        self.inputHost = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.inputHost.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputHost.setFont(font)
        self.inputHost.setObjectName("inputHost")
        self.horizontalLayoutTop.addWidget(self.inputHost)
        self.lbUser = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbUser.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbUser.setFont(font)
        self.lbUser.setObjectName("lbUser")
        self.horizontalLayoutTop.addWidget(self.lbUser)
        self.inputUser = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.inputUser.setEnabled(True)
        self.inputUser.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputUser.setFont(font)
        self.inputUser.setObjectName("inputUser")
        self.horizontalLayoutTop.addWidget(self.inputUser)
        self.lbPass = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbPass.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbPass.setFont(font)
        self.lbPass.setObjectName("lbPass")
        self.horizontalLayoutTop.addWidget(self.lbPass)
        self.inputPass = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.inputPass.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputPass.setFont(font)
        self.inputPass.setObjectName("inputPass")
        self.horizontalLayoutTop.addWidget(self.inputPass)
        self.lbPort = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbPort.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbPort.setFont(font)
        self.lbPort.setObjectName("lbPort")
        self.horizontalLayoutTop.addWidget(self.lbPort)
        self.inputPort = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.inputPort.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inputPort.setFont(font)
        self.inputPort.setObjectName("inputPort")
        self.horizontalLayoutTop.addWidget(self.inputPort)
        self.btnConnect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnConnect.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnConnect.setFont(font)
        self.btnConnect.setObjectName("btnConnect")
        self.horizontalLayoutTop.addWidget(self.btnConnect)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 210, 1121, 391))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(5, 10, 5, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.folderServer = QtWidgets.QTreeView(self.horizontalLayoutWidget_2)
        self.folderServer.setObjectName("folderServer")
        self.horizontalLayout_2.addWidget(self.folderServer)
        self.folderLocal = QtWidgets.QTreeView(self.horizontalLayoutWidget_2)
        self.folderLocal.setObjectName("folderLocal")
        self.horizontalLayout_2.addWidget(self.folderLocal)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 40, 1121, 171))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayoutBottom = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayoutBottom.setContentsMargins(5, 10, 5, 0)
        self.horizontalLayoutBottom.setSpacing(10)
        self.horizontalLayoutBottom.setObjectName("horizontalLayoutBottom")
        self.textStatus = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.textStatus.setEnabled(False)
        self.textStatus.setObjectName("textStatus")
        self.horizontalLayoutBottom.addWidget(self.textStatus)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 600, 1121, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_4)
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdit_2.setObjectName("menuEdit_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionReport_a_bug = QtWidgets.QAction(MainWindow)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTP Client by Hoangsang17th"))
        self.lbHost.setText(_translate("MainWindow", "Host:"))
        self.lbUser.setText(_translate("MainWindow", "Username:"))
        self.lbPass.setText(_translate("MainWindow", "Password:"))
        self.lbPort.setText(_translate("MainWindow", "Port:"))
        self.btnConnect.setText(_translate("MainWindow", "QuickConnect"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit_2.setTitle(_translate("MainWindow", "Edit"))
        self.actionReport_a_bug.setText(_translate("MainWindow", "Report a bug ..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
