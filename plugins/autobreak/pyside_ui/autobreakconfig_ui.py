# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autobreakconfig.ui'
#
# Created: Sat Mar 29 21:52:12 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(297, 264)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 276, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.maxLengthLabel = QtGui.QLabel(self.layoutWidget)
        self.maxLengthLabel.setObjectName("maxLengthLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.maxLengthLabel)
        self.maxLengthSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.maxLengthSpinBox.setMaximum(10000)
        self.maxLengthSpinBox.setProperty("value", 60)
        self.maxLengthSpinBox.setObjectName("maxLengthSpinBox")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.maxLengthSpinBox)
        self.targetLengthSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.targetLengthSpinBox.setMaximum(10000)
        self.targetLengthSpinBox.setProperty("value", 49)
        self.targetLengthSpinBox.setObjectName("targetLengthSpinBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.targetLengthSpinBox)
        self.targetLengthLabel = QtGui.QLabel(self.layoutWidget)
        self.targetLengthLabel.setObjectName("targetLengthLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.targetLengthLabel)
        self.minLengthLabel = QtGui.QLabel(self.layoutWidget)
        self.minLengthLabel.setObjectName("minLengthLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.minLengthLabel)
        self.minLengthSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.minLengthSpinBox.setMaximum(10000)
        self.minLengthSpinBox.setProperty("value", 15)
        self.minLengthSpinBox.setObjectName("minLengthSpinBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.minLengthSpinBox)
        self.minLegLengthLabel = QtGui.QLabel(self.layoutWidget)
        self.minLegLengthLabel.setObjectName("minLegLengthLabel")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.minLegLengthLabel)
        self.minLegLengthSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.minLegLengthSpinBox.setMinimum(2)
        self.minLegLengthSpinBox.setMaximum(10000)
        self.minLegLengthSpinBox.setProperty("value", 3)
        self.minLegLengthSpinBox.setObjectName("minLegLengthSpinBox")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.minLegLengthSpinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.targetLengthSpinBox, self.minLengthSpinBox)
        Dialog.setTabOrder(self.minLengthSpinBox, self.maxLengthSpinBox)
        Dialog.setTabOrder(self.maxLengthSpinBox, self.minLegLengthSpinBox)
        Dialog.setTabOrder(self.minLegLengthSpinBox, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Choose autobreak parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxLengthLabel.setText(QtGui.QApplication.translate("Dialog", "max length", None, QtGui.QApplication.UnicodeUTF8))
        self.targetLengthLabel.setText(QtGui.QApplication.translate("Dialog", "target length", None, QtGui.QApplication.UnicodeUTF8))
        self.minLengthLabel.setText(QtGui.QApplication.translate("Dialog", "min length", None, QtGui.QApplication.UnicodeUTF8))
        self.minLegLengthLabel.setText(QtGui.QApplication.translate("Dialog", "min distance to xover", None, QtGui.QApplication.UnicodeUTF8))
