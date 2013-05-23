import cadnano, util
util.qtWrapImport('QtGui', globals(), ['QIcon', 'QPixmap', 'QAction'])

from pyinterp import MyInterpreter
#from autobreakconfig import AutobreakConfig
from cadnanoconsole import CadnanoAPI


class ConsoleHandler(object):
    def __init__(self, document, window):
        self.doc, self.win = document, window
        icon10 = QIcon()
        # Not (!) using qt resources as compiled in ui/mainwindow/icons.qrc.
        # Plugins should be "plugable" and not dependent on re-combiling resources
        # or otherwise re-configuring the exisitng resource hierarchy.
        # PS: If this is not reliable, consider using 
        #     icon_path = os.getcwd() + "/plugins/cadnano_console/console_32x32.png"
        icon_path = "plugins/cadnano_console/console_32x32.png"
        icon10.addPixmap(QPixmap(icon_path), QIcon.Normal, QIcon.Off)
        self.actionOpenConsole = QAction(window)
        self.actionOpenConsole.setIcon(icon10)
        self.actionOpenConsole.setText('Console')
        self.actionOpenConsole.setToolTip("Open cadnano console interface.")
        self.actionOpenConsole.setObjectName("actionOpenConsole")
        self.actionOpenConsole.triggered.connect(self.actionOpenConsoleSlot)
        self.win.menuPlugins.addAction(self.actionOpenConsole)
        # add to main tool bar
        self.win.topToolBar.insertAction(self.win.actionFiltersLabel, self.actionOpenConsole)
        #self.win.topToolBar.insertSeparator(self.win.actionFiltersLabel)
        self.consoleWindow = None
        self.Api = None

    def actionOpenConsoleSlot(self):
        """
        Opens the cadnano2 console.
        Performance: Only load the api when the console is first opened.
        Notice: locals are not updated upon loading a new design. This may cause issues.
        """
        win = self.consoleWindow = MyInterpreter(None)
        self.consoleWindow.show()
        terp = self.interpreter = self.consoleWindow.textEdit
        # Setting interpreter locals:
        # NOTICE: LOCALS ARE CURRENTLY NOT UPDATED 
        # Variables can be made easily accessible for interpreter reference in either of two ways:
        # 1) terp.terp.interpreterLocals['myvar'] = 'some string'
        # 2) terp.updateInterpreterLocals(myvar, "varname")
        # If no second argument is passed then myvar must be referenced as "<classname>_object", e.g.
        # terp.updateInterpreterLocals(app) # app can be refered to with CadnanoQt_object
        # You can import all local variables, either to a dict in the interpreters locals, 
        # or populating it with all locals:
        #terp.updateInterpreterLocals(locals(), "app_locals")  # locals accessible via app_locals['varname']
        #terp.interpreterLocals.update(locals()) # all locals directly available via varname
        doc = self.doc
        part = self.doc.controller().activePart()
        app = cadnano.app() # should return the app singleton.
        if not self.Api:
            self.Api = CadnanoAPI()
        api = self.Api



def documentWindowWasCreatedSlot(doc, win):
    doc.consoleHandler = ConsoleHandler(doc, win)

# Initialization
for c in cadnano.app().documentControllers:
    doc, win = c.document(), c.window()
    doc.consoleHandler = ConsoleHandler(doc, win)
cadnano.app().documentWindowWasCreatedSignal.connect(documentWindowWasCreatedSlot)
