import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from FTPClient import Ui_MainWindow
import ftplib
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # self.uic.btnOk.clicked.connect(self.loader)
        # self.uic.btnCancel.clicked.connect(self.main_win.close)

    def loader(self):
        self.uic.textEdit.setText("I'm not Iron man")

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())