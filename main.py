from PyQt5.QtWidgets import QApplication
import sys
from downloader.MangaEden import MangaEden
from gui.mainwindow import MainWindow
import json
from downloader.download_engine import DownloadEngine
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

def main3():
    prova = DownloadEngine('http://www.mangawindow.com/manga/to-love-ru-darkness', 'downloader.MangaWindow.MangaWindow',
                           "https{0,1}://(www.mangawindow.com)/manga/([a-zA-Z-+]+)")
    print(prova)
    print(prova.is_valid)
    prova.prepare_engine()


if __name__ == "__main__":
    main3()
