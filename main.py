from PyQt5.QtWidgets import QApplication
import sys
from downloader.MangaEden import MangaEden
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

def main2():
    test = MangaEden("http://www.mangaeden.com/it-manga/dragon-ball/", "/tmp/")
    test.extract_all_chapters_url()
    for d in test.chapters_url:
        print(d)


if __name__ == "__main__":
    main()
