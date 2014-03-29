# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addseq.ui'
#
# Created: Sat Mar 29 21:40:01 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddSeqDialog(object):
    def setupUi(self, AddSeqDialog):
        AddSeqDialog.setObjectName("AddSeqDialog")
        AddSeqDialog.resize(500, 500)
        AddSeqDialog.setModal(True)
        self.dialogGridLayout = QtGui.QGridLayout(AddSeqDialog)
        self.dialogGridLayout.setObjectName("dialogGridLayout")
        self.tabWidget = QtGui.QTabWidget(AddSeqDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabStandard = QtGui.QWidget()
        self.tabStandard.setObjectName("tabStandard")
        self.standardTabGridLayout = QtGui.QGridLayout(self.tabStandard)
        self.standardTabGridLayout.setObjectName("standardTabGridLayout")
        self.groupBox = QtGui.QGroupBox(self.tabStandard)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.standardTabGridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.standardTabGridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.standardTabGridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabStandard, "")
        self.tabCustom = QtGui.QWidget()
        self.tabCustom.setObjectName("tabCustom")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabCustom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.seqTextEdit = QtGui.QTextEdit(self.tabCustom)
        self.seqTextEdit.setObjectName("seqTextEdit")
        self.verticalLayout_2.addWidget(self.seqTextEdit)
        self.tabWidget.addTab(self.tabCustom, "")
        self.dialogGridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.customButtonBox = QtGui.QDialogButtonBox(AddSeqDialog)
        self.customButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        self.customButtonBox.setCenterButtons(True)
        self.customButtonBox.setObjectName("customButtonBox")
        self.dialogGridLayout.addWidget(self.customButtonBox, 1, 0, 1, 1)

        self.retranslateUi(AddSeqDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.customButtonBox, QtCore.SIGNAL("rejected()"), AddSeqDialog.reject)
        QtCore.QObject.connect(self.customButtonBox, QtCore.SIGNAL("clicked(QAbstractButton*)"), AddSeqDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AddSeqDialog)
        AddSeqDialog.setTabOrder(self.customButtonBox, self.tabWidget)
        AddSeqDialog.setTabOrder(self.tabWidget, self.seqTextEdit)

    def retranslateUi(self, AddSeqDialog):
        AddSeqDialog.setWindowTitle(QtGui.QApplication.translate("AddSeqDialog", "Choose a sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStandard), QtGui.QApplication.translate("AddSeqDialog", "Standard", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCustom), QtGui.QApplication.translate("AddSeqDialog", "Custom", None, QtGui.QApplication.UnicodeUTF8))

