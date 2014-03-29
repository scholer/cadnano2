# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'latticetype.ui'
#
# Created: Sat Mar 29 21:39:25 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LatticeType(object):
    def setupUi(self, LatticeType):
        LatticeType.setObjectName("LatticeType")
        LatticeType.resize(215, 80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LatticeType.sizePolicy().hasHeightForWidth())
        LatticeType.setSizePolicy(sizePolicy)
        LatticeType.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(LatticeType)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(LatticeType)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(LatticeType)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LatticeType)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LatticeType.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LatticeType.reject)
        QtCore.QMetaObject.connectSlotsByName(LatticeType)

    def retranslateUi(self, LatticeType):
        LatticeType.setWindowTitle(QtGui.QApplication.translate("LatticeType", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LatticeType", "Is this a square lattice design?", None, QtGui.QApplication.UnicodeUTF8))

