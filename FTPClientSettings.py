# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FTPClientSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsWindow(object):
    def setupUi(self, settingsWindow):
        settingsWindow.setObjectName("settingsWindow")
        settingsWindow.resize(640, 391)
        self.centralwidget = QtWidgets.QWidget(settingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutTab = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutTab.setContentsMargins(10, 5, 10, 5)
        self.layoutTab.setObjectName("layoutTab")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConnect = QtWidgets.QWidget()
        self.tabConnect.setObjectName("tabConnect")
        self.formLayoutWidget = QtWidgets.QWidget(self.tabConnect)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 381))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 0)
        self.formLayout.setObjectName("formLayout")
        self.inputPortConn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputPortConn.setMinimumSize(QtCore.QSize(0, 30))
        self.inputPortConn.setObjectName("inputPortConn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputPortConn)
        self.inputHostConn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputHostConn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.inputHostConn.setFont(font)
        self.inputHostConn.setObjectName("inputHostConn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputHostConn)
        self.lbHostConn = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbHostConn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbHostConn.setFont(font)
        self.lbHostConn.setObjectName("lbHostConn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbHostConn)
        self.inputUserConn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputUserConn.setMinimumSize(QtCore.QSize(0, 30))
        self.inputUserConn.setObjectName("inputUserConn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputUserConn)
        self.lbUsernameConn = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbUsernameConn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbUsernameConn.setFont(font)
        self.lbUsernameConn.setObjectName("lbUsernameConn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbUsernameConn)
        self.inputPassConn = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputPassConn.setMinimumSize(QtCore.QSize(0, 30))
        self.inputPassConn.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassConn.setObjectName("inputPassConn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputPassConn)
        self.lbPasswordConn = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbPasswordConn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbPasswordConn.setFont(font)
        self.lbPasswordConn.setObjectName("lbPasswordConn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbPasswordConn)
        self.lbPortConn = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbPortConn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbPortConn.setFont(font)
        self.lbPortConn.setObjectName("lbPortConn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbPortConn)
        self.lbViewConn = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbViewConn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.lbViewConn.setFont(font)
        self.lbViewConn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbViewConn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbViewConn.setObjectName("lbViewConn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.lbViewConn)
        self.tabWidget.addTab(self.tabConnect, "")
        self.tabTransfers = QtWidgets.QWidget()
        self.tabTransfers.setObjectName("tabTransfers")
        self.tabWidget.addTab(self.tabTransfers, "")
        self.tabInterface = QtWidgets.QWidget()
        self.tabInterface.setObjectName("tabInterface")
        self.tabWidget.addTab(self.tabInterface, "")
        self.tabDebug = QtWidgets.QWidget()
        self.tabDebug.setObjectName("tabDebug")
        self.tabWidget.addTab(self.tabDebug, "")
        self.layoutTab.addWidget(self.tabWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 350, 641, 38))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 5, 10, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSave = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        settingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(settingsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settingsWindow)

    def retranslateUi(self, settingsWindow):
        _translate = QtCore.QCoreApplication.translate
        settingsWindow.setWindowTitle(_translate("settingsWindow", "Settings -FTPClient"))
        self.lbHostConn.setText(_translate("settingsWindow", "Host:"))
        self.lbUsernameConn.setText(_translate("settingsWindow", "Username:"))
        self.lbPasswordConn.setText(_translate("settingsWindow", "Password:"))
        self.lbPortConn.setText(_translate("settingsWindow", "Port:"))
        self.lbViewConn.setText(_translate("settingsWindow", "Default Connection Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConnect), _translate("settingsWindow", "Connection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTransfers), _translate("settingsWindow", "Transfers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInterface), _translate("settingsWindow", "Interface"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDebug), _translate("settingsWindow", "Debug"))
        self.btnSave.setText(_translate("settingsWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsWindow = QtWidgets.QMainWindow()
    ui = Ui_settingsWindow()
    ui.setupUi(settingsWindow)
    settingsWindow.show()
    sys.exit(app.exec_())