from PyQt5.QtWidgets import QApplication
import sys
from gui.mainwindow import MainWindow
import json
from gui.ui_MainWindow import Ui_MainWindow


__author__ = 'pablo'
from downloader import MangaWindow

def main():
    json_data = open('configuration.json')
    data = json.load(json_data)

    app = QApplication(sys.argv)
    window = MainWindow(data)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
