from PyQt5.QtCore import pyqtSlot, QCoreApplication, QDir
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QPushButton, QFileDialog
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
        self.ui.destination_line_edit.textChanged.connect(self.on_destination_line_edit_finish)
        self.ui.destination_push_button.clicked.connect(self.on_destination_button_clicked)

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

    def on_destination_button_clicked(self):
        filename = QFileDialog.getExistingDirectory(self, QCoreApplication.translate('NewDialog', 'Output folder'),
                                                    QDir.homePath(),
                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.ui.destination_line_edit.setText(filename)