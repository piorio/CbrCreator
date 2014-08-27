from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui.new_dialog import NewDialog
from gui.ui_MainWindow import Ui_MainWindow

__author__ = 'pablo'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Connect
        self.ui.action_Quit.triggered.connect(self.quit)
        self.ui.action_New.triggered.connect(self.on_new)

    @pyqtSlot()
    def quit(self):
        QApplication.quit()

    @pyqtSlot()
    def on_new(self):
        new_dialog = NewDialog()
        new_dialog.exec()