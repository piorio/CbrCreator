# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_dialog.ui'
#
# Created: Wed Aug 27 13:51:20 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 249)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 200, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.url_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.url_label.setObjectName("url_label")
        self.horizontalLayout.addWidget(self.url_label)
        self.url_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url_line_edit.sizePolicy().hasHeightForWidth())
        self.url_line_edit.setSizePolicy(sizePolicy)
        self.url_line_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.url_line_edit.setObjectName("url_line_edit")
        self.horizontalLayout.addWidget(self.url_line_edit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 80, 401, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.engine_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.engine_label.setObjectName("engine_label")
        self.horizontalLayout_2.addWidget(self.engine_label)
        self.downloader_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.downloader_combo_box.setMinimumSize(QtCore.QSize(300, 0))
        self.downloader_combo_box.setObjectName("downloader_combo_box")
        self.horizontalLayout_2.addWidget(self.downloader_combo_box)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 140, 401, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.out_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.out_label.setObjectName("out_label")
        self.horizontalLayout_3.addWidget(self.out_label)
        self.destination_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destination_line_edit.sizePolicy().hasHeightForWidth())
        self.destination_line_edit.setSizePolicy(sizePolicy)
        self.destination_line_edit.setMinimumSize(QtCore.QSize(275, 0))
        self.destination_line_edit.setObjectName("destination_line_edit")
        self.horizontalLayout_3.addWidget(self.destination_line_edit)
        self.destination_push_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destination_push_button.sizePolicy().hasHeightForWidth())
        self.destination_push_button.setSizePolicy(sizePolicy)
        self.destination_push_button.setMinimumSize(QtCore.QSize(10, 10))
        self.destination_push_button.setMaximumSize(QtCore.QSize(20, 16777215))
        self.destination_push_button.setObjectName("destination_push_button")
        self.horizontalLayout_3.addWidget(self.destination_push_button)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New"))
        self.url_label.setText(_translate("Dialog", "URL:"))
        self.engine_label.setText(_translate("Dialog", "Downloader:"))
        self.out_label.setText(_translate("Dialog", "Destination:"))
        self.destination_push_button.setText(_translate("Dialog", "..."))

