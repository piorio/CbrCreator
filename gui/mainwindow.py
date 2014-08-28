from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
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
        self.ui.actionDownload_chapters.triggered.connect(self.on_download_chapters_triggered)

        #Setup default value
        self.ui.chapters_table_widget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def quit(self):
        QApplication.quit()

    @pyqtSlot()
    def on_new(self):
        new_dialog = NewDialog()
        if new_dialog.exec() == QDialog.Accepted:
            self.ui.actionDownload_chapters.setEnabled(True)
            self.ui.url_line_edit.setText(new_dialog.url)


    def on_download_chapters_triggered(self):
        print('Download')