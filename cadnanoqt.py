# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php

"""
cadnanoqt
Created by Jonathan deWerd on 2012-01-11.
"""
import util, sys, os
import cadnano
from code import interact
util.qtWrapImport('QtGui', globals(),  ['qApp', 'QApplication', 'QIcon',\
                                        'QUndoGroup'])
util.qtWrapImport('QtCore', globals(), ['QObject', 'QCoreApplication', 'Qt',\
                                        'QEventLoop', 'pyqtSignal'])

class CadnanoQt(QObject):
    dontAskAndJustDiscardUnsavedChanges = False
    shouldPerformBoilerplateStartupScript = False
    documentWasCreatedSignal = pyqtSignal(object)  # doc
    documentWindowWasCreatedSignal = pyqtSignal(object, object)  # doc, window

    def __init__(self, argv):
        self.argv = argv
        if QCoreApplication.instance() == None:
            self.qApp = QApplication(argv)
            assert(QCoreApplication.instance() != None)
            self.qApp.setOrganizationDomain("cadnano.org")
        else:
            self.qApp = qApp
        super(CadnanoQt, self).__init__()
        from views.preferences import Preferences
        self.prefs = Preferences()
        self.qApp.setWindowIcon(QIcon('ui/mainwindow/images/cadnano2-app-icon.png'))
        self.documentControllers = set()  # Open documents
        self.activeDocument = None
        self.vh = {}  # Newly created VirtualHelix register here by idnum.
        self.vhi = {}
        self.partItem = None
        self.sharedApp = self


    def ignoreEnv(self):
        return os.environ.get('CADNANO_IGNORE_ENV_VARS_EXCEPT_FOR_ME', False)

    def finishInit(self):
        self.d = self.newDocument(isFirstNewDoc=True)
        if os.environ.get('CADNANO_DISCARD_UNSAVED', False) and not self.ignoreEnv():
            self.sharedApp.dontAskAndJustDiscardUnsavedChanges = True
        if os.environ.get('CADNANO_DEFAULT_DOCUMENT', False) and not self.ignoreEnv():
            self.sharedApp.shouldPerformBoilerplateStartupScript = True
        cadnano.loadAllPlugins()
        if "-i" in self.argv:
            print "Welcome to cadnano's debug mode!"
            print "Some handy locals:"
            print "\ta\tcadnano.app() (the shared cadnano application object)"
            print "\td()\tthe last created Document"
            def d():
                return self.d

            print "\tw()\tshortcut for d().controller().window()"
            def w():
                return self.d.controller().window()

            print "\tp()\tshortcut for d().selectedPart()"
            def p():
                return self.d.selectedPart()

            print "\tpi()\tthe PartItem displaying p()"
            def pi():
                return w().pathroot.partItemForPart(p())

            print "\tvh(i)\tshortcut for p().virtualHelix(i)"
            def vh(vhref):
                return p().virtualHelix(vhref)

            print "\tvhi(i)\tvirtualHelixItem displaying vh(i)"
            def vhi(vhref):
                partitem = pi()
                vHelix = vh(vhref)
                return partitem.vhItemForVH(vHelix)
                
            print "\tquit()\tquit (for when the menu fails)"
            print "\tgraphicsItm.findChild()  see help(pi().findChild)"
            interact('', local={'a':self, 'd':d, 'w':w,\
                                'p':p, 'pi':pi, 'vh':vh, 'vhi':vhi,\
                                })
        # else:
        #     self.exec_()

    def isInMaya(self):
        return QCoreApplication.instance().applicationName().contains(
                                                    "Maya", Qt.CaseInsensitive)
    def isGui(self):
        return True
    
    def exec_(self):
        if hasattr(self, 'qApp'):
            self.mainEventLoop = QEventLoop()
            self.mainEventLoop.exec_()
            #self.qApp.exec_()

    def newDocument(self, isFirstNewDoc=False):
        from controllers.documentcontroller import DocumentController
        defaultFile = os.environ.get('CADNANO_DEFAULT_DOCUMENT', None)
        if defaultFile and isFirstNewDoc:
            defaultFile = path.expanduser(defaultFile)
            defaultFile = path.expandvars(defaultFile)
            dc = DocumentController()
            doc = dc.document()
            from model.io.decoder import decode
            decode(doc, file(defaultFile).read())
            print "Loaded default document: %s" % doc
        else:
            docCtrlrCount = len(self.documentControllers)
            if docCtrlrCount == 0:  # first dc
                # dc adds itself to app.documentControllers
                dc = DocumentController()
            elif docCtrlrCount == 1:  # dc already exists
                dc = list(self.documentControllers)[0]
                dc.newDocument()  # tell it to make a new doucment
        return dc.document()

    def prefsClicked(self):
        self.prefs.showDialog()
