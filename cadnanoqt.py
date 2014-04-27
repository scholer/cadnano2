# pylint: disable-msg=C0103,C0303,C0301,W0108,C0111
# -*- coding: utf-8 -*-
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

About the cadnano qt initialization sequence:
    main.py                     calls cadnano.initAppWithGui(), then cadnano.app() to get a reference to the newly initialized app, sharedApp.
    cadnano.initAppWithGui()    instances sharedApp=CadnanoQt(appArgs) followed by sharedApp.finishInit()
    CadnanoQt.__init__()        instances self.qApp = QApplication(argv). I.e. sharedApp.qApp
    CadnanoQt.finishInit()      instances self.d = self.newDocument(isFirstNewDoc=True). This is an "empty" document window.
                                There is exactly ONE cadnano documentwindow (aka mainwindow) per open document.
                                I don't think self.d is ever used for anything, but in theory it would hold the last created document.
                                Also calls cadnano.loadAllPlugins() and conditionally creates a code.interact prompt if -i in argv
    CadnanoQt.newDocument()     Instances DocumentController()
    DocumentController init     Instances self._document = Document(), self.win = DocumentWindow(docCtrlr=self),
                                emits app().documentWindowWasCreatedSignal.emit(self._document, self.win) (connected to slots in the plugins)
                                shows the main documentwindow with self.win.show() plus does some extra stuff if in maya,
                                connects signals, and adds it self to app().documentControllers .
    DocumentWindow init         Sets up the mainwindow's ui elements and connects signals, nothing unexpected.
    main.py                     Calls app.exec_() which just starts the main application event loop with self.qApp.exec_()

And that's just about it. The rest is handled by the event loop.


Regarding using IPython as interactive console in cadnano, the conclusion is that
if a user wants this, he/she can just call main.py with ipython instead of python as:
    ipython --gui=qt -- main.py -i

### OLD IPYTHON NOTES: ###
If using IPython console, the IPython interpreter must be quit() before quitting cadnano.
EDIT: Using IPython is actually rather complicated (althrough easier in the newest dev version):
-- http://stackoverflow.com/questions/16737323/embedding-ipython-into-a-pyqt4-app
-- http://stackoverflow.com/questions/14739425/how-to-embed-ipython-kernel-into-pyqt4-program
-- http://ipython.org/ipython-doc/dev/interactive/qtconsole.html (note: it has to be dev; not in stable yet)


## NOTE: At this point, the qt application loop has not actually started.
## It might be better (safer) to hook up a qtconsole
## especially if loading ipython or doing other advanced stuff

Despite a lot of attemts, all attempts with using IPython has introduced an issue
where quitting the application before iPython will keep the thread running in the
background.
According to the docs, it seems the intended approach is to use ipython's
IPython.lib.inputhook and lib.guisupport modules to configure and launch
the GUI (Qt, Wx, GTK, Tk, ) using python's native PyOSInputHook.
This would make the code for enabling interactive mode with IPython much overtly elaborate,
and exceed the benefits -- and it also seems to require a newer version of IPython...
Attemted IPython methods include embed(), embed_kernel(), start_kernel(),
 IPython.frontend.terminal.embed.InteractiveShellEmbed()() # formerly IPython.Shell.IPShellEmbeded
IPython.embed(user_ns=ns) # Naive approach. Makes it hard to properly terminate the thread.
Maybe the better solution is to just start cadnano with ipython from the command line?
This works: (the -- ensures that -i is interpreted as an argument to main.py and not ipython)
 ipython --gui=qt -- main.py -i


"""
import os
import cadnano
import util
import cadnano_api

try:
    qt_selection = util.chosenQtFramework or util.find_available_qt_framework()
except AttributeError:
    msg = "AttributeError: %s - this cadnano might be too old for this plugin, aborting load." % (e, )
    print msg
    qt_selection = None

try:
    # On windows, readline can be provided via the pyreadline package (will create a 'readline' alias file during installation...)
    import readline     # should be imported first.
except ImportError:
    print "(readline/rlcompleter not available...)"
    readline = None
else:
    # If no ImportError. rlcompleter is standard lib.
    import rlcompleter

import code

util.qtWrapImport('QtGui', globals(),  ['qApp', 'QApplication', 'QIcon',
                                        'QUndoGroup'])
util.qtWrapImport('QtCore', globals(), ['QObject', 'QCoreApplication', 'Qt',
                                        'QEventLoop', 'pyqtSignal'])
#util.qtWrapImport('QtCore', globals(), ['SIGNAL', 'SLOT', 'pyqtSlot'])

class CadnanoQt(QObject):
    """
    This is the application base object, aka sharedApp or cadnano.app().
    This is NOT a QApplication, but the parent of self.qApp = QApplication.
    Additional prominent child objects of a CadnanoQt objects (self):
        self.documentControllers :  set of document controllers (will currently holds just one documentcontroller)

    """
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
        self.d = None

    def ignoreEnv(self):
        return os.environ.get('CADNANO_IGNORE_ENV_VARS_EXCEPT_FOR_ME', False)

    def finishInit(self):
        self.d = self.newDocument(isFirstNewDoc=True)
        os.environ['CADNANO_DISCARD_UNSAVED'] = 'True' ## added by Nick
        if os.environ.get('CADNANO_DISCARD_UNSAVED', False) and not self.ignoreEnv():
            self.sharedApp.dontAskAndJustDiscardUnsavedChanges = True
        if os.environ.get('CADNANO_DEFAULT_DOCUMENT', False) and not self.ignoreEnv():
            self.sharedApp.shouldPerformBoilerplateStartupScript = True
        cadnano.loadAllPlugins()

        if "-i" in self.argv:
            print "Welcome to cadnano's debug mode!"

            # All api shortcut functions have been factored out to the utils module.
            # (So the functions are easier to access if running cadnano as part of a larger script!)
            ns = cadnano_api.get_api(self)

            if readline:
                print "Enabling line-completion for standard code.interact mode...\n"
                # This is required, even when invoked via ipython, to get completion for a, d, etc.
                readline.set_completer(rlcompleter.Completer(ns).complete) # Makes it work :)
                readline.parse_and_bind("tab: complete") # Not strictly required when invoked via ipython.
            else:
                print "No readline/completer available..."
            if qt_selection == 'pyside':
                print "NOTE NOTE: There seems to be an issue running cadnano with PySide in interactive mode.\
If the UI does not load properly, hit Ctrl+D to exit the interactive prompt. \
You should still be able to run interactive mode with ipython with:   ipython --gui=qt -- main.py -i   \
(tested with ipython 1.1.0 with PySide on Windows)"
            print ns['cadnanohelp']
            code.interact("", local=ns)
            print "Interactive mode with code.interact complete..."

        # else:
        #     self.exec_()  # exec_() is invoked conditionally in main.py depending on command line arguments.

    def isInMaya(self):
        appName = QCoreApplication.instance().applicationName()
        try:
            return appName.contains("Maya", Qt.CaseInsensitive)
        except AttributeError:
            return "maya" in appName.lower()
    def isGui(self):
        return True

    def exec_(self):
        """
        Starts main application loop. Invoked by the main.py bootstrapping script.
        # Notice: CadnanoQt is NOT a QtApplication, it is a QtObject. self.qApp is the application.
        """
        if hasattr(self, 'qApp'):
            #self.mainEventLoop = QEventLoop()
            #self.mainEventLoop.exec_() # Why this?
            self.qApp.exec_()           # This works better than the above mainEventLoop.exec_(), at least on linux.

    def newDocument(self, isFirstNewDoc=False, fp=None):
        """
        Creates a new document, ensuring that a document controller is also instantiated if required.
        If isFirstNewDoc is True, a new documentController is always instantiated.
        A new documentController will create a new document during __init__().
        This method is called by finishInit() to ensure a document is created on application init.
        """
        from controllers.documentcontroller import DocumentController
        defaultFile = fp or os.environ.get('CADNANO_DEFAULT_DOCUMENT', None)
        if defaultFile and isFirstNewDoc:
            defaultFile = os.path.expanduser(defaultFile)
            defaultFile = os.path.expandvars(defaultFile)
            dc = DocumentController()
            doc = dc.document()
            from model.io.decoder import decode
            decode(doc, open(defaultFile).read())
            print "Loaded default document: %s" % doc
        else:
            dc = next(iter(self.documentControllers), None)
            # cadnano currently only supports ONE documentcontroller per app instance, controlling exactly ONE document.
            if dc:                  # if a documentcontroller already exists
                dc.newDocument()    # currently, this just empties the existing document object.
            else: # first dc
                # A DocumentController creates a new doc during init and adds itself to app.documentControllers:
                dc = DocumentController()
        return dc.document()

    def prefsClicked(self):
        self.prefs.showDialog()
