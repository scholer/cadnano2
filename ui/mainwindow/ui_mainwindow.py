# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Mar 29 21:38:27 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 792)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStatusTip("")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(7)
        self.splitter.setObjectName("splitter")
        self.sliceGraphicsView = CustomQGraphicsView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliceGraphicsView.sizePolicy().hasHeightForWidth())
        self.sliceGraphicsView.setSizePolicy(sizePolicy)
        self.sliceGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.sliceGraphicsView.setBaseSize(QtCore.QSize(480, 0))
        self.sliceGraphicsView.setMouseTracking(True)
        self.sliceGraphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.sliceGraphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.sliceGraphicsView.setLineWidth(0)
        self.sliceGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sliceGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sliceGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.sliceGraphicsView.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.sliceGraphicsView.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.sliceGraphicsView.setResizeAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.sliceGraphicsView.setObjectName("sliceGraphicsView")
        self.pathGraphicsView = CustomQGraphicsView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathGraphicsView.sizePolicy().hasHeightForWidth())
        self.pathGraphicsView.setSizePolicy(sizePolicy)
        self.pathGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.pathGraphicsView.setMouseTracking(True)
        self.pathGraphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pathGraphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.pathGraphicsView.setLineWidth(0)
        self.pathGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.TextAntialiasing)
        self.pathGraphicsView.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.pathGraphicsView.setObjectName("pathGraphicsView")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.topToolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topToolBar.sizePolicy().hasHeightForWidth())
        self.topToolBar.setSizePolicy(sizePolicy)
        self.topToolBar.setBaseSize(QtCore.QSize(550, 0))
        self.topToolBar.setIconSize(QtCore.QSize(24, 24))
        self.topToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.topToolBar.setObjectName("topToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.topToolBar)
        self.rightToolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightToolBar.sizePolicy().hasHeightForWidth())
        self.rightToolBar.setSizePolicy(sizePolicy)
        self.rightToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.rightToolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rightToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.rightToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.rightToolBar.setObjectName("rightToolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.rightToolBar)
        self.leftToolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftToolBar.sizePolicy().hasHeightForWidth())
        self.leftToolBar.setSizePolicy(sizePolicy)
        self.leftToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.leftToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.leftToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.leftToolBar.setObjectName("leftToolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.leftToolBar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPlugins = QtGui.QMenu(self.menubar)
        self.menuPlugins.setObjectName("menuPlugins")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/filetools/new"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/filetools/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filetools/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setIcon(icon2)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_a_Copy = QtGui.QAction(MainWindow)
        self.actionSave_a_Copy.setObjectName("actionSave_a_Copy")
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionSVG = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/filetools/svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSVG.setIcon(icon3)
        self.actionSVG.setObjectName("actionSVG")
        self.actionX3D = QtGui.QAction(MainWindow)
        self.actionX3D.setObjectName("actionX3D")
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionNewHoneycombPart = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/parttools/new-honeycomb"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewHoneycombPart.setIcon(icon4)
        self.actionNewHoneycombPart.setObjectName("actionNewHoneycombPart")
        self.actionPathBreak = QtGui.QAction(MainWindow)
        self.actionPathBreak.setCheckable(True)
        self.actionPathBreak.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pathtools/break"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathBreak.setIcon(icon5)
        self.actionPathBreak.setObjectName("actionPathBreak")
        self.actionPathSelect = QtGui.QAction(MainWindow)
        self.actionPathSelect.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pathtools/select"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathSelect.setIcon(icon6)
        self.actionPathSelect.setObjectName("actionPathSelect")
        self.actionSliceFirst = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/slicetools/go-first"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSliceFirst.setIcon(icon7)
        self.actionSliceFirst.setObjectName("actionSliceFirst")
        self.actionSliceLast = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/slicetools/go-last"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSliceLast.setIcon(icon8)
        self.actionSliceLast.setObjectName("actionSliceLast")
        self.actionPathErase = QtGui.QAction(MainWindow)
        self.actionPathErase.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/pathtools/erase"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathErase.setIcon(icon9)
        self.actionPathErase.setObjectName("actionPathErase")
        self.actionPathPencil = QtGui.QAction(MainWindow)
        self.actionPathPencil.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/pathtools/force"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathPencil.setIcon(icon10)
        self.actionPathPencil.setObjectName("actionPathPencil")
        self.actionPathInsertion = QtGui.QAction(MainWindow)
        self.actionPathInsertion.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/pathtools/insert"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathInsertion.setIcon(icon11)
        self.actionPathInsertion.setObjectName("actionPathInsertion")
        self.actionNewSquarePart = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/parttools/new-square"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewSquarePart.setIcon(icon12)
        self.actionNewSquarePart.setObjectName("actionNewSquarePart")
        self.actionPathSkip = QtGui.QAction(MainWindow)
        self.actionPathSkip.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/pathtools/skip"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathSkip.setIcon(icon13)
        self.actionPathSkip.setObjectName("actionPathSkip")
        self.actionRenumber = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/slicetools/renumber"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRenumber.setIcon(icon14)
        self.actionRenumber.setObjectName("actionRenumber")
        self.actionPathPaint = QtGui.QAction(MainWindow)
        self.actionPathPaint.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/pathtools/paint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathPaint.setIcon(icon15)
        self.actionPathPaint.setObjectName("actionPathPaint")
        self.actionPathAddSeq = QtGui.QAction(MainWindow)
        self.actionPathAddSeq.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/pathtools/addseq"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathAddSeq.setIcon(icon16)
        self.actionPathAddSeq.setObjectName("actionPathAddSeq")
        self.actionExportStaples = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/filetools/csv"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportStaples.setIcon(icon17)
        self.actionExportStaples.setObjectName("actionExportStaples")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionModify = QtGui.QAction(MainWindow)
        self.actionModify.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/pathtools/modify"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModify.setIcon(icon18)
        self.actionModify.setObjectName("actionModify")
        self.actionCadnanoWebsite = QtGui.QAction(MainWindow)
        self.actionCadnanoWebsite.setObjectName("actionCadnanoWebsite")
        self.actionFeedback = QtGui.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionFilterPart = QtGui.QAction(MainWindow)
        self.actionFilterPart.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/parttools/filter-part"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterPart.setIcon(icon19)
        self.actionFilterPart.setObjectName("actionFilterPart")
        self.actionFilterEndpoint = QtGui.QAction(MainWindow)
        self.actionFilterEndpoint.setCheckable(True)
        self.actionFilterEndpoint.setChecked(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/parttools/filter-endpoint"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterEndpoint.setIcon(icon20)
        self.actionFilterEndpoint.setObjectName("actionFilterEndpoint")
        self.actionFilterXover = QtGui.QAction(MainWindow)
        self.actionFilterXover.setCheckable(True)
        self.actionFilterXover.setChecked(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/parttools/filter-xover"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterXover.setIcon(icon21)
        self.actionFilterXover.setText("")
        self.actionFilterXover.setObjectName("actionFilterXover")
        self.actionFiltersLabel = QtGui.QAction(MainWindow)
        self.actionFiltersLabel.setEnabled(False)
        self.actionFiltersLabel.setObjectName("actionFiltersLabel")
        self.actionFilterStrand = QtGui.QAction(MainWindow)
        self.actionFilterStrand.setCheckable(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/parttools/filter-strand"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterStrand.setIcon(icon22)
        self.actionFilterStrand.setObjectName("actionFilterStrand")
        self.actionFilterHandle = QtGui.QAction(MainWindow)
        self.actionFilterHandle.setCheckable(True)
        self.actionFilterHandle.setChecked(False)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/parttools/filter-handle"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterHandle.setIcon(icon23)
        self.actionFilterHandle.setObjectName("actionFilterHandle")
        self.actionFilterScaf = QtGui.QAction(MainWindow)
        self.actionFilterScaf.setCheckable(True)
        self.actionFilterScaf.setChecked(True)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/parttools/filter-scaf"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterScaf.setIcon(icon24)
        self.actionFilterScaf.setObjectName("actionFilterScaf")
        self.actionFilterStap = QtGui.QAction(MainWindow)
        self.actionFilterStap.setCheckable(True)
        self.actionFilterStap.setChecked(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/parttools/filter-stap"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterStap.setIcon(icon25)
        self.actionFilterStap.setObjectName("actionFilterStap")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAutoStaple = QtGui.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/pathtools/autostaple"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAutoStaple.setIcon(icon26)
        self.actionAutoStaple.setObjectName("actionAutoStaple")
        self.topToolBar.addAction(self.actionNew)
        self.topToolBar.addAction(self.actionOpen)
        self.topToolBar.addAction(self.actionSave)
        self.topToolBar.addAction(self.actionSVG)
        self.topToolBar.addAction(self.actionExportStaples)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.actionNewHoneycombPart)
        self.topToolBar.addAction(self.actionNewSquarePart)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.actionAutoStaple)
        self.topToolBar.addAction(self.actionFiltersLabel)
        self.topToolBar.addAction(self.actionFilterScaf)
        self.topToolBar.addAction(self.actionFilterStap)
        self.topToolBar.addAction(self.actionFilterHandle)
        self.topToolBar.addAction(self.actionFilterEndpoint)
        self.topToolBar.addAction(self.actionFilterXover)
        self.topToolBar.addAction(self.actionFilterStrand)
        self.rightToolBar.addAction(self.actionPathSelect)
        self.rightToolBar.addAction(self.actionPathPencil)
        self.rightToolBar.addAction(self.actionPathBreak)
        self.rightToolBar.addAction(self.actionPathInsertion)
        self.rightToolBar.addAction(self.actionPathSkip)
        self.rightToolBar.addAction(self.actionPathPaint)
        self.rightToolBar.addAction(self.actionPathAddSeq)
        self.leftToolBar.addAction(self.actionSliceFirst)
        self.leftToolBar.addAction(self.actionSliceLast)
        self.leftToolBar.addAction(self.actionRenumber)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionModify)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "cadnano", None, QtGui.QApplication.UnicodeUTF8))
        self.topToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Main Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.rightToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Path Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.leftToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Slice Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("MainWindow", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_a_Copy.setText(QtGui.QApplication.translate("MainWindow", "Save a Copy...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSVG.setText(QtGui.QApplication.translate("MainWindow", "SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.actionX3D.setText(QtGui.QApplication.translate("MainWindow", "X3D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewHoneycombPart.setText(QtGui.QApplication.translate("MainWindow", "Honeycomb", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewHoneycombPart.setToolTip(QtGui.QApplication.translate("MainWindow", "Click to add new part with honeycomb lattice", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setText(QtGui.QApplication.translate("MainWindow", "Break Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setIconText(QtGui.QApplication.translate("MainWindow", "Break", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setToolTip(QtGui.QApplication.translate("MainWindow", "(B)reak Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setShortcut(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setIconText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setToolTip(QtGui.QApplication.translate("MainWindow", "Select Tool (v)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setShortcut(QtGui.QApplication.translate("MainWindow", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceFirst.setText(QtGui.QApplication.translate("MainWindow", "First", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceFirst.setToolTip(QtGui.QApplication.translate("MainWindow", "Move the slice bar to the first position.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceLast.setText(QtGui.QApplication.translate("MainWindow", "Last", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceLast.setToolTip(QtGui.QApplication.translate("MainWindow", "Move the slice bar to the last position.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathErase.setText(QtGui.QApplication.translate("MainWindow", "Erase", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathErase.setToolTip(QtGui.QApplication.translate("MainWindow", "(E)rase Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPencil.setText(QtGui.QApplication.translate("MainWindow", "Pencil", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPencil.setToolTip(QtGui.QApplication.translate("MainWindow", "Pe(n)cil Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPencil.setShortcut(QtGui.QApplication.translate("MainWindow", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathInsertion.setText(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathInsertion.setToolTip(QtGui.QApplication.translate("MainWindow", "(I)nsert Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathInsertion.setShortcut(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSquarePart.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSquarePart.setToolTip(QtGui.QApplication.translate("MainWindow", "Click to add new part with square lattice", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSkip.setText(QtGui.QApplication.translate("MainWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSkip.setToolTip(QtGui.QApplication.translate("MainWindow", "(S)kip Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSkip.setShortcut(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenumber.setText(QtGui.QApplication.translate("MainWindow", "Rnum", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenumber.setToolTip(QtGui.QApplication.translate("MainWindow", "Renumber Slice helices according to helix ordering in Path panel.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPaint.setText(QtGui.QApplication.translate("MainWindow", "Paint", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPaint.setToolTip(QtGui.QApplication.translate("MainWindow", "(P)aint Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPaint.setShortcut(QtGui.QApplication.translate("MainWindow", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathAddSeq.setText(QtGui.QApplication.translate("MainWindow", "Seq", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathAddSeq.setToolTip(QtGui.QApplication.translate("MainWindow", "(A)dd Sequence Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathAddSeq.setShortcut(QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportStaples.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportStaples.setToolTip(QtGui.QApplication.translate("MainWindow", "export oligos as *.CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+,", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModify.setText(QtGui.QApplication.translate("MainWindow", "Modify mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModify.setToolTip(QtGui.QApplication.translate("MainWindow", "Modify mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCadnanoWebsite.setText(QtGui.QApplication.translate("MainWindow", "cadnano Website", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFeedback.setText(QtGui.QApplication.translate("MainWindow", "Feedback", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterPart.setText(QtGui.QApplication.translate("MainWindow", "Parts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterPart.setToolTip(QtGui.QApplication.translate("MainWindow", "Part-selection mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterEndpoint.setToolTip(QtGui.QApplication.translate("MainWindow", "(E)ndpoints", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterEndpoint.setShortcut(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterXover.setToolTip(QtGui.QApplication.translate("MainWindow", "(X)overs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterXover.setShortcut(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFiltersLabel.setText(QtGui.QApplication.translate("MainWindow", "Selectable:", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFiltersLabel.setToolTip(QtGui.QApplication.translate("MainWindow", "Selection Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterStrand.setToolTip(QtGui.QApplication.translate("MainWindow", "stran(D)s", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterStrand.setShortcut(QtGui.QApplication.translate("MainWindow", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterHandle.setToolTip(QtGui.QApplication.translate("MainWindow", "(H)andles", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterHandle.setShortcut(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterScaf.setToolTip(QtGui.QApplication.translate("MainWindow", "s(C)affold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterScaf.setShortcut(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterStap.setToolTip(QtGui.QApplication.translate("MainWindow", "s(T)aple", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterStap.setShortcut(QtGui.QApplication.translate("MainWindow", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About cadnano", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoStaple.setText(QtGui.QApplication.translate("MainWindow", "AutoStaple", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoStaple.setToolTip(QtGui.QApplication.translate("MainWindow", "Create staple strands complementary to existing scaffold.", None, QtGui.QApplication.UnicodeUTF8))

from views.customqgraphicsview import CustomQGraphicsView
import icons_rc
