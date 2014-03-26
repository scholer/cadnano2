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
try:
    ## If using IPython console, the IPython interpreter must be quit() before quitting cadnano.
    ## EDIT: Using IPython is actually rather complicated (althrough easier in the newest dev version):
    ## -- http://stackoverflow.com/questions/16737323/embedding-ipython-into-a-pyqt4-app
    ## -- http://stackoverflow.com/questions/14739425/how-to-embed-ipython-kernel-into-pyqt4-program
    ## -- http://ipython.org/ipython-doc/dev/interactive/qtconsole.html (note: it has to be dev; not in stable yet)
    raise ImportError("IPython currently disabled, since it makes quitting super flaky.")
    import IPython
except ImportError:
    print "(IPython not available, trying to import readline+rlcompleter...)"
    IPython = None
    try:
        # On windows, readline can be provided via the pyreadline package (will create a 'readline' alias file during installation...)
        import readline     # should be imported first, I believe...
    except ImportError:
        print "(readline/rlcompleter not available...)"
        readline = None
    else:
        # If no ImportError...
        import rlcompleter  # refers to readline during import. rlcompleter
        # readline.parse_and_bind("tab: complete")

#from code import interact
import code

util.qtWrapImport('QtGui', globals(),  ['qApp', 'QApplication', 'QIcon',\
                                        'QUndoGroup'])
util.qtWrapImport('QtCore', globals(), ['QObject', 'QCoreApplication', 'Qt',\
                                        'QEventLoop', 'pyqtSignal'])
#util.qtWrapImport('QtCore', globals(), ['SIGNAL', 'SLOT', 'pyqtSlot'])

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

        ## NOTE: At this point, the qt application loop has not actually started.
        ## It might be better (safer) to hook up a qtconsole
        ## especially if loading ipython or doing other advanced stuff

        if "-i" in self.argv:
            print "Welcome to cadnano's debug mode!"
            print "Some handy locals:"
            print "\ta\tcadnano.app() (the shared cadnano application object)"

            print "\tdc()\tthe document controller"
            def dc():
                # self.documentControllers is a set. This is an easy way to return an arbitrary element from a set:
                return next(iter(self.documentControllers), None)

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

            def enableAutocomplete(ns):
                readline.set_completer(rlcompleter.Completer(ns).complete)
                readline.parse_and_bind("tab: complete")

            print "\tquit()\tquit (for when the menu fails)"
            print "\tgraphicsItm.findChild()  see help(pi().findChild)"
            print "Local modules include: model, controllers, ui, views, data and plugins."
            print "dc() controls file creation/loading/saving."
            print "Use dc().openAfterMaybeSaveCallback(<filepath>) to open a new file."
            print "If dc() is None, use a.newDocument([fp=filepath]) to create a new controller."
            print "As always, dir() and help() are helpful."
            print "For more detail, use inspect.getsource(<class or function>)"
            print "Note that app quit/exit is a bit flaky when interactive mode is on."
            print "This might be because the application loop has not actually been initiated."

            ns = {'a':self, 'd':d, 'dc':dc, 'w':w, 'p':p, 'pi':pi, 'vh':vh, 'vhi':vhi,
                  'enableAutocomplete':enableAutocomplete, 'stdQuit':quit, 'stdExit':exit}
            if IPython:
                print "Starting iPython embedded console...\n"
                IPython.embed(user_ns=ns) # Take care, makes it hard to terminate the thread.
                #IPython.embed_kernel(user_ns=ns) # Uh, not what you want... you need a qtconsole to connect.
                #IPython.start_kernel(user_ns=ns) # Only available in ipython >0.13
                #from IPython.frontend.terminal.embed import InteractiveShellEmbed
                #self.ipshell = InteractiveShellEmbed()
                #self.ipshell() # Still, if you first exit cadnano and then quit() in terminal the thread does not terminate.
            elif readline:
                print "Starting standard code.interact mode...\n"
                readline.set_completer(rlcompleter.Completer(ns).complete) # Makes it work :)
                readline.parse_and_bind("tab: complete")
                code.interact('', local=ns)
                #readline.set_completer(rlcompleter.Completer(ns).complete)
                #readline.parse_and_bind("tab: complete")
                print "Interactive mode complete..."
            else:
                print "No readline/completer available..."
            print "Interactive mode complete!"
        # else:
        #     self.exec_()

    def isInMaya(self):
        return QCoreApplication.instance().applicationName().contains(
                                                    "Maya", Qt.CaseInsensitive)
    def isGui(self):
        return True

    def exec_(self):
        """
        Starts main application loop. Invoked by the main.py bootstrapping script.
        # Notice: CadnanoQt is NOT a QtApplication, it is a QtObject. self.qApp is the application.
        """
        if hasattr(self, 'qApp'):
            #self.mainEventLoop = QEventLoop()
            #self.connect(self.qApp, SIGNAL("lastWindowClosed()"), self.qApp, SLOT("quit()")) # added by RS - but doesn't work... and not required if using qApp.exec_()
            #self.mainEventLoop.exec_()
            self.qApp.exec_() # Yeah, this works much better than the above mainEventLoop.exec_(). Who added the extra QEventLoop code ??

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
            defaultFile = path.expanduser(defaultFile)
            defaultFile = path.expandvars(defaultFile)
            dc = DocumentController()
            doc = dc.document()
            from model.io.decoder import decode
            decode(doc, file(defaultFile).read())
            print "Loaded default document: %s" % doc
        else:
            dc = next(iter(self.documentControllers), None)
            if dc: # dc already exists
                dc.newDocument()
            else: # first dc
                # dc creates a new doc during init and adds itself to app.documentControllers:
                dc = DocumentController()
        return dc.document()

    def prefsClicked(self):
        self.prefs.showDialog()
