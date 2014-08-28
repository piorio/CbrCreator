from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QPushButton
from gui.ui_NewDialog import Ui_Dialog

__author__ = 'pablo'


class NewDialog(QDialog):
    def __init__(self):
        super(NewDialog, self).__init__()

        self.url = None
        self.destination = None

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Disable the OK button
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        #Connect
        self.ui.url_line_edit.textEdited.connect(self.on_url_line_edit_finish)
        self.ui.destination_line_edit.textEdited.connect(self.on_destination_line_edit_finish)

    @pyqtSlot(str)
    def on_url_line_edit_finish(self, text):
        self.url = self.ui.url_line_edit.text()
        if self.url is not None and self.destination is not None and len(self.url) > 0 and len(self.destination) > 0:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    @pyqtSlot(str)
    def on_destination_line_edit_finish(self, text):
        self.destination = self.ui.destination_line_edit.text()
        if self.url is not None and self.destination is not None and len(self.url) > 0 and len(self.destination) > 0:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)