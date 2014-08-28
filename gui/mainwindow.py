from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem
from downloader.MangaWindow import MangaWindow
from gui.new_dialog import NewDialog
from gui.ui_MainWindow import Ui_MainWindow

__author__ = 'pablo'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.url = None
        self.destination = None
        self.engine = None

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
        new_dialog = NewDialog(['MangaWindow'])
        if new_dialog.exec() == QDialog.Accepted:
            self.ui.actionDownload_chapters.setEnabled(True)

            self.url = new_dialog.url
            self.destination = new_dialog.destination
            self.engine = new_dialog.engine
            self.ui.url_line_edit.setText(self.url)

    @pyqtSlot()
    def on_download_chapters_triggered(self):

        #engine_to_use = __import__('downloader.'+self.engine)
        #engine_to_use = getattr(engine_to_use, self.engine)

        engine_to_use = MainWindow.get_class('downloader.' + self.engine + '.' + self.engine)
        downloader = engine_to_use(self.url, self.destination)

        urls_list = downloader.extract_all_chapters_url()
        self.fill_table(urls_list)

    def fill_table(self, urls_list):
        row_index = 0
        self.ui.chapters_table_widget.setRowCount(len(urls_list))
        print(urls_list)
        for chapter, url in urls_list.items():
            chapter_item = QTableWidgetItem(chapter)
            url_item = QTableWidgetItem(url)
            download_item = QTableWidgetItem('YES')

            self.ui.chapters_table_widget.setItem(row_index, 0, chapter_item)
            self.ui.chapters_table_widget.setItem(row_index, 1, download_item)
            self.ui.chapters_table_widget.setItem(row_index, 2, url_item)

            row_index += 1

        self.ui.chapters_table_widget.resizeColumnsToContents()
        self.ui.chapters_table_widget.sortItems(0)

    def get_class( kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m