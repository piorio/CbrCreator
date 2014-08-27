from PyQt5.QtWidgets import QDialog
from gui.ui_NewDialog import Ui_Dialog

__author__ = 'pablo'


class NewDialog(QDialog):
    def __init__(self):
        super(NewDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)