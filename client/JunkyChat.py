# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kouta\JunkyChat\client\JunkyChat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1073, 601)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1081, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1079, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.MessageLogs = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.MessageLogs.setGeometry(QtCore.QRect(250, 30, 821, 521))
        self.MessageLogs.setBaseSize(QtCore.QSize(0, 0))
        self.MessageLogs.setStyleSheet("background:#343a40;\n"
"color:white;\n"
"font: 7pt \"Microsoft JhengHei UI\";")
        self.MessageLogs.setScaledContents(False)
        self.MessageLogs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.MessageLogs.setObjectName("MessageLogs")
        self.CreateTalkRoomForm = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.CreateTalkRoomForm.setGeometry(QtCore.QRect(250, 0, 441, 31))
        self.CreateTalkRoomForm.setObjectName("CreateTalkRoomForm")
        self.CreateTalkRoom = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CreateTalkRoom.setGeometry(QtCore.QRect(690, -10, 141, 41))
        self.CreateTalkRoom.setObjectName("CreateTalkRoom")
        self.TalkRooms = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.TalkRooms.setGeometry(QtCore.QRect(0, 30, 251, 521))
        self.TalkRooms.setObjectName("TalkRooms")
        item_0 = QtWidgets.QTreeWidgetItem(self.TalkRooms)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(0, 0, 251, 31))
        self.label.setStyleSheet("font: 25 12pt \"Yu Gothic\";\n"
"text-align:center;\n"
"background:#a9a9a9;\n"
"color:white;")
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.MessageForm = QtWidgets.QTextEdit(Dialog)
        self.MessageForm.setGeometry(QtCore.QRect(0, 550, 931, 51))
        self.MessageForm.setAutoFillBackground(False)
        self.MessageForm.setStyleSheet("font: 25 11pt \"Yu Gothic UI Light\";\n"
"background:#f8f9fa;\n"
"color:black;")
        self.MessageForm.setObjectName("MessageForm")
        self.Send = QtWidgets.QPushButton(Dialog)
        self.Send.setGeometry(QtCore.QRect(930, 550, 141, 51))
        self.Send.setStyleSheet("font: 18pt \"MS UI Gothic\";\n"
"background:#17a2b8;\n"
"color:white;")
        self.Send.setObjectName("Send")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.MessageLogs.setText(_translate("Dialog", "<html><head/><body><p>メッセージ(送信で更新されます)</p></body></html>"))
        self.CreateTalkRoom.setText(_translate("Dialog", "トークルームを作成する"))
        self.TalkRooms.headerItem().setText(0, _translate("Dialog", "公式"))
        __sortingEnabled = self.TalkRooms.isSortingEnabled()
        self.TalkRooms.setSortingEnabled(False)
        self.TalkRooms.topLevelItem(0).setText(0, _translate("Dialog", "ロビー"))
        self.TalkRooms.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">トークルーム一覧</span></p></body></html>"))
        self.MessageForm.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic UI Light\'; font-size:11pt; font-weight:24; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.MessageForm.setPlaceholderText(_translate("Dialog", "メッセージを入力"))
        self.Send.setText(_translate("Dialog", "送信"))
