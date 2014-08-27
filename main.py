from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from gui.mainwindow import MainWindow
from gui.ui_MainWindow import Ui_MainWindow

__author__ = 'pablo'
from downloader import mangawindow

def main():

    #test = mangawindow.MangaWindow('http://www.mangawindow.com/manga/original-work-warau-kangofu', '/tmp/prova')
    #test.extract_all_chapters_url()
    #test.download_each_chapter()
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
