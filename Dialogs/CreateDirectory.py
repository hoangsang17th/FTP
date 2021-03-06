# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateDirectory.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createFolderWindow(object):
    def setupUi(self, createFolderWindow):
        createFolderWindow.setObjectName("createFolderWindow")
        createFolderWindow.resize(400, 150)
        createFolderWindow.setMinimumSize(QtCore.QSize(400, 150))
        createFolderWindow.setMaximumSize(QtCore.QSize(400, 150))
        self.centralwidget = QtWidgets.QWidget(createFolderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbCreateDirectory = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbCreateDirectory.setFont(font)
        self.lbCreateDirectory.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lbCreateDirectory.setLineWidth(2)
        self.lbCreateDirectory.setMidLineWidth(2)
        self.lbCreateDirectory.setTextFormat(QtCore.Qt.AutoText)
        self.lbCreateDirectory.setScaledContents(False)
        self.lbCreateDirectory.setWordWrap(True)
        self.lbCreateDirectory.setObjectName("lbCreateDirectory")
        self.verticalLayout.addWidget(self.lbCreateDirectory)
        self.inputCreateDirectory = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inputCreateDirectory.setMinimumSize(QtCore.QSize(0, 30))
        self.inputCreateDirectory.setObjectName("inputCreateDirectory")
        self.verticalLayout.addWidget(self.inputCreateDirectory)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 110, 231, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOK = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        createFolderWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(createFolderWindow)
        QtCore.QMetaObject.connectSlotsByName(createFolderWindow)

    def retranslateUi(self, createFolderWindow):
        _translate = QtCore.QCoreApplication.translate
        createFolderWindow.setWindowTitle(_translate("createFolderWindow", "Create Directory"))
        self.lbCreateDirectory.setText(_translate("createFolderWindow", "Please enter the name of the directory which should be created:"))
        self.inputCreateDirectory.setText(_translate("createFolderWindow", "/"))
        self.btnOK.setText(_translate("createFolderWindow", "OK"))
        self.btnCancel.setText(_translate("createFolderWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createFolderWindow = QtWidgets.QMainWindow()
    ui = Ui_createFolderWindow()
    ui.setupUi(createFolderWindow)
    createFolderWindow.show()
    sys.exit(app.exec_())
