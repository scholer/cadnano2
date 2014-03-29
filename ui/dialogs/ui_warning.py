# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created: Sat Mar 29 21:40:25 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName("Warning")
        Warning.setWindowModality(QtCore.Qt.ApplicationModal)
        Warning.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Warning)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.title = QtGui.QLabel(Warning)
        self.title.setGeometry(QtCore.QRect(20, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.message = QtGui.QLabel(Warning)
        self.message.setGeometry(QtCore.QRect(20, 80, 361, 151))
        self.message.setWordWrap(True)
        self.message.setObjectName("message")

        self.retranslateUi(Warning)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Warning.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Warning.reject)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        Warning.setWindowTitle(QtGui.QApplication.translate("Warning", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Warning", "Warning", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setText(QtGui.QApplication.translate("Warning", "Text here.", None, QtGui.QApplication.UnicodeUTF8))

