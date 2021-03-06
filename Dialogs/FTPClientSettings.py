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
        settingsWindow.resize(640, 270)
        settingsWindow.setMinimumSize(QtCore.QSize(640, 270))
        settingsWindow.setMaximumSize(QtCore.QSize(640, 270))
        self.centralwidget = QtWidgets.QWidget(settingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutTab = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutTab.setContentsMargins(10, 5, 10, 5)
        self.layoutTab.setObjectName("layoutTab")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConnect = QtWidgets.QWidget()
        self.tabConnect.setObjectName("tabConnect")
        self.formLayoutWidget = QtWidgets.QWidget(self.tabConnect)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 172))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 5, 10, 0)
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
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbViewConn.setFont(font)
        self.lbViewConn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbViewConn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbViewConn.setObjectName("lbViewConn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.lbViewConn)
        self.tabWidget.addTab(self.tabConnect, "")
        self.tabTransfers = QtWidgets.QWidget()
        self.tabTransfers.setObjectName("tabTransfers")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabTransfers)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 601, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbViewTransfers = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbViewTransfers.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbViewTransfers.setFont(font)
        self.lbViewTransfers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbViewTransfers.setAlignment(QtCore.Qt.AlignCenter)
        self.lbViewTransfers.setObjectName("lbViewTransfers")
        self.verticalLayout.addWidget(self.lbViewTransfers)
        self.tabUpDown = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabUpDown.setObjectName("tabUpDown")
        self.tabUploads = QtWidgets.QWidget()
        self.tabUploads.setObjectName("tabUploads")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tabUploads)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 581, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioAskU = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioAskU.setObjectName("radioAskU")
        self.horizontalLayout_2.addWidget(self.radioAskU)
        self.radioSkipU = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioSkipU.setObjectName("radioSkipU")
        self.horizontalLayout_2.addWidget(self.radioSkipU)
        self.radioOverwriteU = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioOverwriteU.setObjectName("radioOverwriteU")
        self.horizontalLayout_2.addWidget(self.radioOverwriteU)
        self.tabUpDown.addTab(self.tabUploads, "")
        self.tabDownloads = QtWidgets.QWidget()
        self.tabDownloads.setObjectName("tabDownloads")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tabDownloads)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 581, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioAskD = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioAskD.setObjectName("radioAskD")
        self.horizontalLayout_3.addWidget(self.radioAskD)
        self.radioSkipD = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioSkipD.setObjectName("radioSkipD")
        self.horizontalLayout_3.addWidget(self.radioSkipD)
        self.radioOverwriteD = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioOverwriteD.setObjectName("radioOverwriteD")
        self.horizontalLayout_3.addWidget(self.radioOverwriteD)
        self.tabUpDown.addTab(self.tabDownloads, "")
        self.verticalLayout.addWidget(self.tabUpDown)
        self.tabWidget.addTab(self.tabTransfers, "")
        self.layoutTab.addWidget(self.tabWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 230, 641, 38))
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
        self.btnCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        settingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(settingsWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabUpDown.setCurrentIndex(1)
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
        self.lbViewTransfers.setText(_translate("settingsWindow", "Default file exists action"))
        self.radioAskU.setText(_translate("settingsWindow", "Ask for action"))
        self.radioSkipU.setText(_translate("settingsWindow", "Skip"))
        self.radioOverwriteU.setText(_translate("settingsWindow", "Overwrite"))
        self.tabUpDown.setTabText(self.tabUpDown.indexOf(self.tabUploads), _translate("settingsWindow", "Uploads"))
        self.radioAskD.setText(_translate("settingsWindow", "Ask for action"))
        self.radioSkipD.setText(_translate("settingsWindow", "Skip"))
        self.radioOverwriteD.setText(_translate("settingsWindow", "Overwrite"))
        self.tabUpDown.setTabText(self.tabUpDown.indexOf(self.tabDownloads), _translate("settingsWindow", "Downloads"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTransfers), _translate("settingsWindow", "Transfers"))
        self.btnSave.setText(_translate("settingsWindow", "Save"))
        self.btnCancel.setText(_translate("settingsWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsWindow = QtWidgets.QMainWindow()
    ui = Ui_settingsWindow()
    ui.setupUi(settingsWindow)
    settingsWindow.show()
    sys.exit(app.exec_())
