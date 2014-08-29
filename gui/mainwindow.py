from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem, QMessageBox
from downloader.MangaWindow import MangaWindow
from gui.new_dialog import NewDialog
from gui.ui_MainWindow import Ui_MainWindow
from multiprocessing import Process

__author__ = 'pablo'


class MainWindow(QMainWindow):
    def __init__(self, configuration):
        super(MainWindow, self).__init__()

        self.url = None
        self.destination = None
        self.engine = None
        self.downloader = None
        self.configuration = configuration
        self.plugins_list = []

        for plugin in self.configuration['plugins']:
            self.plugins_list.append(plugin)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Connect
        self.ui.action_Quit.triggered.connect(self.quit)
        self.ui.action_New.triggered.connect(self.on_new)
        self.ui.actionDownload_chapters.triggered.connect(self.on_download_chapters_triggered)
        self.ui.actionStart_download.triggered.connect(self.on_start_download_triggered)

        #Setup default value
        self.ui.chapters_table_widget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def quit(self):
        QApplication.quit()

    @pyqtSlot()
    def on_new(self):
        new_dialog = NewDialog(self.plugins_list)
        if new_dialog.exec() == QDialog.Accepted:
            self.ui.actionDownload_chapters.setEnabled(True)

            self.url = new_dialog.url
            self.destination = new_dialog.destination
            self.engine = new_dialog.engine
            self.ui.url_line_edit.setText(self.url)

    @pyqtSlot()
    def on_download_chapters_triggered(self):

        engine_to_use = MainWindow.get_class('downloader.' + self.engine + '.' + self.engine)
        self.downloader = engine_to_use(self.url, self.destination)

        urls_list = self.downloader.extract_all_chapters_url()
        self.fill_table(urls_list)
        self.ui.actionStart_download.setEnabled(True)

    @pyqtSlot()
    def on_start_download_triggered(self):
        process_list = []
        table_size = self.ui.chapters_table_widget.rowCount()
        for i in range(0, table_size):
            if self.ui.chapters_table_widget.item(i, 1).checkState() == Qt.Checked:
                chapter = self.ui.chapters_table_widget.item(i, 0).text()
                url = self.ui.chapters_table_widget.item(i, 2).text()
                print("{}->{}".format(chapter, url))
                p = Process(target=self.downloader.download_specific_chapter, args=(url, chapter,))
                p.start()
                process_list.append(p)

        for p in process_list:
            print("JOIN " + str(p))
            p.join()

        QMessageBox.information(self, 'Download', 'Finish')


    def fill_table(self, urls_list):
        row_index = 0
        self.ui.chapters_table_widget.setRowCount(len(urls_list))
        print(urls_list)
        for chapter, url in urls_list.items():
            chapter_item = QTableWidgetItem(chapter)
            url_item = QTableWidgetItem(url)
            download_item = QTableWidgetItem('TO DOWNLOAD')
            download_item.setCheckState(Qt.Checked)

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