# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Aug 28 13:51:49 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setObjectName("url_label")
        self.horizontalLayout.addWidget(self.url_label)
        self.url_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.url_line_edit.setReadOnly(True)
        self.url_line_edit.setObjectName("url_line_edit")
        self.horizontalLayout.addWidget(self.url_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.chapters_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.chapters_table_widget.setObjectName("chapters_table_widget")
        self.chapters_table_widget.setColumnCount(3)
        self.chapters_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.chapters_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.chapters_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.chapters_table_widget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.chapters_table_widget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 19))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Tool = QtWidgets.QMenu(self.menubar)
        self.menu_Tool.setObjectName("menu_Tool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_New = QtWidgets.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionDownload_chapters = QtWidgets.QAction(MainWindow)
        self.actionDownload_chapters.setEnabled(False)
        self.actionDownload_chapters.setObjectName("actionDownload_chapters")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Tool.addAction(self.actionDownload_chapters)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tool.menuAction())
        self.toolBar.addAction(self.action_New)
        self.toolBar.addAction(self.actionDownload_chapters)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CbrCreator"))
        self.url_label.setText(_translate("MainWindow", "URL:"))
        item = self.chapters_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CHAPTER"))
        item = self.chapters_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DOWNLOAD"))
        item = self.chapters_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "URL"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Tool.setTitle(_translate("MainWindow", "&Tool"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.action_New.setText(_translate("MainWindow", "&New..."))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.actionDownload_chapters.setText(_translate("MainWindow", "Download chapters"))

