# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/preferences.ui'
#
# Created: Wed Jul 20 15:20:45 2011
#      by: PyQt4 UI code generator snapshot-4.8.3-fbc8b1362812
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(440, 272)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Preferences)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.zoomSpeedLabel = QtGui.QLabel(Preferences)
        self.zoomSpeedLabel.setObjectName(_fromUtf8("zoomSpeedLabel"))
        self.gridLayout.addWidget(self.zoomSpeedLabel, 4, 0, 1, 1)
        self.zoomSpeedSlider = QtGui.QSlider(Preferences)
        self.zoomSpeedSlider.setMaximum(100)
        self.zoomSpeedSlider.setProperty(_fromUtf8("value"), 50)
        self.zoomSpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSpeedSlider.setInvertedAppearance(False)
        self.zoomSpeedSlider.setInvertedControls(False)
        self.zoomSpeedSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSpeedSlider.setTickInterval(0)
        self.zoomSpeedSlider.setObjectName(_fromUtf8("zoomSpeedSlider"))
        self.gridLayout.addWidget(self.zoomSpeedSlider, 4, 1, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 4)
        self.tabWidget = QtGui.QTabWidget(Preferences)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_honeycomb = QtGui.QWidget()
        self.tab_honeycomb.setObjectName(_fromUtf8("tab_honeycomb"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_honeycomb)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.honeycombHLayout = QtGui.QHBoxLayout()
        self.honeycombHLayout.setObjectName(_fromUtf8("honeycombHLayout"))
        self.dimensionsLabel1 = QtGui.QLabel(self.tab_honeycomb)
        self.dimensionsLabel1.setObjectName(_fromUtf8("dimensionsLabel1"))
        self.honeycombHLayout.addWidget(self.dimensionsLabel1)
        self.honeycombGLayout = QtGui.QGridLayout()
        self.honeycombGLayout.setContentsMargins(-1, 3, -1, -1)
        self.honeycombGLayout.setObjectName(_fromUtf8("honeycombGLayout"))
        self.honeycombRowSpinBox = QtGui.QSpinBox(self.tab_honeycomb)
        self.honeycombRowSpinBox.setMinimum(6)
        self.honeycombRowSpinBox.setMaximum(200)
        self.honeycombRowSpinBox.setProperty(_fromUtf8("value"), 30)
        self.honeycombRowSpinBox.setObjectName(_fromUtf8("honeycombRowSpinBox"))
        self.honeycombGLayout.addWidget(self.honeycombRowSpinBox, 0, 0, 1, 1)
        self.honeycombColSpinBox = QtGui.QSpinBox(self.tab_honeycomb)
        self.honeycombColSpinBox.setMinimum(6)
        self.honeycombColSpinBox.setMaximum(200)
        self.honeycombColSpinBox.setProperty(_fromUtf8("value"), 32)
        self.honeycombColSpinBox.setObjectName(_fromUtf8("honeycombColSpinBox"))
        self.honeycombGLayout.addWidget(self.honeycombColSpinBox, 0, 1, 1, 1)
        self.hRowsLabel = QtGui.QLabel(self.tab_honeycomb)
        self.hRowsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hRowsLabel.setObjectName(_fromUtf8("hRowsLabel"))
        self.honeycombGLayout.addWidget(self.hRowsLabel, 1, 0, 1, 1)
        self.hColsLabel = QtGui.QLabel(self.tab_honeycomb)
        self.hColsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hColsLabel.setObjectName(_fromUtf8("hColsLabel"))
        self.honeycombGLayout.addWidget(self.hColsLabel, 1, 1, 1, 1)
        self.honeycombBaseSpinBox = QtGui.QSpinBox(self.tab_honeycomb)
        self.honeycombBaseSpinBox.setMinimum(2)
        self.honeycombBaseSpinBox.setMaximum(2000)
        self.honeycombBaseSpinBox.setSingleStep(1)
        self.honeycombBaseSpinBox.setProperty(_fromUtf8("value"), 2)
        self.honeycombBaseSpinBox.setObjectName(_fromUtf8("honeycombBaseSpinBox"))
        self.honeycombGLayout.addWidget(self.honeycombBaseSpinBox, 0, 2, 1, 1)
        self.hBasesLabel = QtGui.QLabel(self.tab_honeycomb)
        self.hBasesLabel.setObjectName(_fromUtf8("hBasesLabel"))
        self.honeycombGLayout.addWidget(self.hBasesLabel, 1, 2, 1, 1)
        self.honeycombHLayout.addLayout(self.honeycombGLayout)
        self.gridLayout_5.addLayout(self.honeycombHLayout, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/part/honeycomb")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_honeycomb, icon, _fromUtf8(""))
        self.tab_square = QtGui.QWidget()
        self.tab_square.setObjectName(_fromUtf8("tab_square"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_square)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.squareHLayout = QtGui.QHBoxLayout()
        self.squareHLayout.setObjectName(_fromUtf8("squareHLayout"))
        self.dimensionsLabel2 = QtGui.QLabel(self.tab_square)
        self.dimensionsLabel2.setObjectName(_fromUtf8("dimensionsLabel2"))
        self.squareHLayout.addWidget(self.dimensionsLabel2)
        self.squareGLayout = QtGui.QGridLayout()
        self.squareGLayout.setContentsMargins(-1, 3, -1, -1)
        self.squareGLayout.setObjectName(_fromUtf8("squareGLayout"))
        self.squareRowsSpinBox = QtGui.QSpinBox(self.tab_square)
        self.squareRowsSpinBox.setMinimum(6)
        self.squareRowsSpinBox.setMaximum(200)
        self.squareRowsSpinBox.setProperty(_fromUtf8("value"), 30)
        self.squareRowsSpinBox.setObjectName(_fromUtf8("squareRowsSpinBox"))
        self.squareGLayout.addWidget(self.squareRowsSpinBox, 0, 0, 1, 1)
        self.squareColsSpinBox = QtGui.QSpinBox(self.tab_square)
        self.squareColsSpinBox.setMinimum(6)
        self.squareColsSpinBox.setMaximum(200)
        self.squareColsSpinBox.setProperty(_fromUtf8("value"), 30)
        self.squareColsSpinBox.setObjectName(_fromUtf8("squareColsSpinBox"))
        self.squareGLayout.addWidget(self.squareColsSpinBox, 0, 1, 1, 1)
        self.sRowsLabel = QtGui.QLabel(self.tab_square)
        self.sRowsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sRowsLabel.setObjectName(_fromUtf8("sRowsLabel"))
        self.squareGLayout.addWidget(self.sRowsLabel, 1, 0, 1, 1)
        self.sColsLabel = QtGui.QLabel(self.tab_square)
        self.sColsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sColsLabel.setObjectName(_fromUtf8("sColsLabel"))
        self.squareGLayout.addWidget(self.sColsLabel, 1, 1, 1, 1)
        self.squareBasesSpinBox = QtGui.QSpinBox(self.tab_square)
        self.squareBasesSpinBox.setMinimum(2)
        self.squareBasesSpinBox.setMaximum(2000)
        self.squareBasesSpinBox.setObjectName(_fromUtf8("squareBasesSpinBox"))
        self.squareGLayout.addWidget(self.squareBasesSpinBox, 0, 2, 1, 1)
        self.sBasesLabel = QtGui.QLabel(self.tab_square)
        self.sBasesLabel.setObjectName(_fromUtf8("sBasesLabel"))
        self.squareGLayout.addWidget(self.sBasesLabel, 1, 2, 1, 1)
        self.squareHLayout.addLayout(self.squareGLayout)
        self.gridLayout_4.addLayout(self.squareHLayout, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/part/square")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_square, icon1, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 4)
        self.zoomfitLabel = QtGui.QLabel(Preferences)
        self.zoomfitLabel.setObjectName(_fromUtf8("zoomfitLabel"))
        self.gridLayout.addWidget(self.zoomfitLabel, 5, 0, 1, 1)
        self.helixAddCheckBox = QtGui.QCheckBox(Preferences)
        self.helixAddCheckBox.setChecked(True)
        self.helixAddCheckBox.setObjectName(_fromUtf8("helixAddCheckBox"))
        self.gridLayout.addWidget(self.helixAddCheckBox, 5, 1, 1, 1)
        self.defaulttoolLabel = QtGui.QLabel(Preferences)
        self.defaulttoolLabel.setObjectName(_fromUtf8("defaulttoolLabel"))
        self.gridLayout.addWidget(self.defaulttoolLabel, 3, 0, 1, 1)
        self.helixReorderCheckBox = QtGui.QCheckBox(Preferences)
        self.helixReorderCheckBox.setChecked(True)
        self.helixReorderCheckBox.setObjectName(_fromUtf8("helixReorderCheckBox"))
        self.gridLayout.addWidget(self.helixReorderCheckBox, 5, 2, 1, 1)
        self.defaulttoolComboBox = QtGui.QComboBox(Preferences)
        self.defaulttoolComboBox.setObjectName(_fromUtf8("defaulttoolComboBox"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/select")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defaulttoolComboBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/pencil")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defaulttoolComboBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/paint")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defaulttoolComboBox.addItem(icon4, _fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/addseq")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defaulttoolComboBox.addItem(icon5, _fromUtf8(""))
        self.gridLayout.addWidget(self.defaulttoolComboBox, 3, 2, 1, 1)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.buttonBox, self.tabWidget)
        Preferences.setTabOrder(self.tabWidget, self.defaulttoolComboBox)
        Preferences.setTabOrder(self.defaulttoolComboBox, self.honeycombRowSpinBox)
        Preferences.setTabOrder(self.honeycombRowSpinBox, self.honeycombColSpinBox)
        Preferences.setTabOrder(self.honeycombColSpinBox, self.squareRowsSpinBox)
        Preferences.setTabOrder(self.squareRowsSpinBox, self.squareColsSpinBox)
        Preferences.setTabOrder(self.squareColsSpinBox, self.zoomSpeedSlider)
        Preferences.setTabOrder(self.zoomSpeedSlider, self.helixAddCheckBox)
        Preferences.setTabOrder(self.helixAddCheckBox, self.helixReorderCheckBox)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomSpeedLabel.setText(QtGui.QApplication.translate("Preferences", "Zoom speed:", None, QtGui.QApplication.UnicodeUTF8))
        self.dimensionsLabel1.setText(QtGui.QApplication.translate("Preferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Default</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dimensions</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.hRowsLabel.setText(QtGui.QApplication.translate("Preferences", "rows", None, QtGui.QApplication.UnicodeUTF8))
        self.hColsLabel.setText(QtGui.QApplication.translate("Preferences", "columns", None, QtGui.QApplication.UnicodeUTF8))
        self.hBasesLabel.setText(QtGui.QApplication.translate("Preferences", "bases (x21)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_honeycomb), QtGui.QApplication.translate("Preferences", "Honeycomb", None, QtGui.QApplication.UnicodeUTF8))
        self.dimensionsLabel2.setText(QtGui.QApplication.translate("Preferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Default</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dimensions</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sRowsLabel.setText(QtGui.QApplication.translate("Preferences", "rows", None, QtGui.QApplication.UnicodeUTF8))
        self.sColsLabel.setText(QtGui.QApplication.translate("Preferences", "columns", None, QtGui.QApplication.UnicodeUTF8))
        self.sBasesLabel.setText(QtGui.QApplication.translate("Preferences", "bases (x32)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_square), QtGui.QApplication.translate("Preferences", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomfitLabel.setText(QtGui.QApplication.translate("Preferences", "Zoom to fit on:", None, QtGui.QApplication.UnicodeUTF8))
        self.helixAddCheckBox.setText(QtGui.QApplication.translate("Preferences", "Helix addition", None, QtGui.QApplication.UnicodeUTF8))
        self.defaulttoolLabel.setText(QtGui.QApplication.translate("Preferences", "Default tool at startup:", None, QtGui.QApplication.UnicodeUTF8))
        self.helixReorderCheckBox.setText(QtGui.QApplication.translate("Preferences", "Helix reordering", None, QtGui.QApplication.UnicodeUTF8))
        self.defaulttoolComboBox.setItemText(0, QtGui.QApplication.translate("Preferences", "Select Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.defaulttoolComboBox.setItemText(1, QtGui.QApplication.translate("Preferences", "Pencil Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.defaulttoolComboBox.setItemText(2, QtGui.QApplication.translate("Preferences", "Paint", None, QtGui.QApplication.UnicodeUTF8))
        self.defaulttoolComboBox.setItemText(3, QtGui.QApplication.translate("Preferences", "Add Seq", None, QtGui.QApplication.UnicodeUTF8))

import dialogicons_rc
