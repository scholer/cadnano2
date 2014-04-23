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

"""

import cadnano

try:
    import readline
    import rlcompleter
except ImportError:
    readline = None

import inspect


def get_api(app=None):
    """
    Returns a namespace dict using app as base.
    app should be a
    If app=None, uses cadnano.app().
    """

    # This needs to be split out to separate module if you want to use cadnano.app()
    # You cannot import cadnano in this module, since that would create cyclic import.
    #if app is None:
    #    app = cadnano.app() # App singleton
    cadnanohelp = """
Some handy locals:
\ta\tcadnano.app() (the shared cadnano application object)
\tdc()\tthe document controller
\td()\tthe last created Document
\tw()\tshortcut for d().controller().window()
\tp()\tshortcut for d().selectedPart()
\tpi()\tthe PartItem displaying p()
\tvh(i)\tshortcut for p().virtualHelix(i)
\tvhi(i)\tvirtualHelixItem displaying vh(i)

\tquit()\tquit (for when the menu fails)
\tgraphicsItm.findChild()  see help(pi().findChild)

dc() controls file creation/loading/saving.
Use dc().openAfterMaybeSaveCallback(<filepath>) to open a new file.
If dc() is None, use a.newDocument([fp=filepath]) to create a new controller.

Local modules available for import include:
    model, controllers, ui, views, data and plugins.

As always, dir() and help() are exceedingly helpful.
For more detail on methods etc. use inspect.getsource(<module, class or function>)

Note that app quit/exit is a bit flaky when interactive mode is on.
(This might be because the application loop has not actually been initiated.)

"""

    ### Basic cadnano object shortcuts ###

    def a():
        return app or cadnano.app()
    def d():
        """
        Shortcut to the current document. The document can hold one (and in theory more) parts.
        """
        return a().d
    def dc():
        """ Shortcut to the current document-controller, which is used to e.g. create new/load/save documents. """
        # self.documentControllers is a set. Using next(iter(<set>)) is an easy way to return an arbitrary element from a set:
        # return next(iter(app.documentControllers), None)
        # Edit: Probably more consistent to use
        try:
            return d().controller()
        except AttributeError:
            pass
    def w():
        """ Shortcut to the window for the current document. """
        return d().controller().window()
    def p():
        """
        Shortcut to the current part. The part contains the virtual helices.
        Corresponds roughly to the set of virtual helices handled by the document).
        Should also be available as dc().activePart()
        """
        return d().selectedPart()
    def pi():
        """ Shortcut to the PartItem(QGraphicsRectItem) UI item representing the current part, p(). """
        return w().pathroot.partItemForPart(p())
    def vh(vhref):
        """ Returns the current part's VirtualHelix given by <vhref>. <vhref> can be an index or a coordinate. """
        return p().virtualHelix(vhref)
    def vhi(vhref):
        """ Returns the VirtualHelixItem(QGraphicsPathItem) UI item representing the virtual helix given by <vhref>. """
        return pi().vhItemForVH(vh(vhref))




    ## Part shortcuts ##

    def get_active_baseIndex():
        """ Returns the active baseindex (usually adjusted by the "slider"). """
        return p().activeBaseIndex()

    def set_active_baseindex(index):
        """ Sets the active baseindex (usually adjusted by the "slider"). """
        p().setActiveBaseIndex(index)

    def get_staplesequences():
        p().getStapleSequences()

    ### Strand shortcuts

    def get_selected_strands():
        selectedStrands = {strand for strandSet, strands in d().selectionDict().items() for strand in strands}
        return selectedStrands


    ### Oligo shortcuts ###

    def get_selected_oligos():
        """
        Return the oligos which are actually selected.
        I.e. what d().selectedOligos() should have been, if it worked as expected.
        (d().selectedOligos() currently returns ALL oligos on the currently selected HELIX)
        Note: You need to actually select a strand (it should appear highlighted/red)
        for this to work, but then I also think it works.

        d()._selectionDict / d().selectionDict() returns a dict-dict construct:
        selectionDict[<strandset>][<strand>]
        """
        # This is what d().selectedOligos() does
        #selectedOs = set()
        #for sS in d().selectionDict().iterkeys():
        #    for strand in sS:                      # here, d().selectedOligos() includes ALL strands in the strandset,
        #         selectedOs.add(strand.oligo())    # where strandset is in sDict if only a single strand is selected.
        #return selectedOs if len(selectedOs) > 0 else None
        selectedOs = {strand.oligo() for strandSet, strands in d().selectionDict().items() for strand in strands}
        return selectedOs


    def get_oligo_colors():
        """
        Returns a set of colors used by the currently selected oligos.
        """
        return {oligo.color() for oligo in get_selected_oligos()}


    def get_oligo_color():
        """
        Returns the color of the currently selected oligo. If more oligos are selected,
        returns the color of an arbitrary.
        If no oligos are selected, returns None
        """
        return next(iter(get_oligo_colors()), None)


    def set_oligos_color(color, enableRedo=True):
        """
        Sets the color of all selected oligos to <color>.
        """
        if isinstance(color, basestring):
            qtWrapImport('QtCore', globals(), ['QString'])
            # PySide uses standard str as QString, but that should not be a problem.
            color = QString(color)
        selectedOs = get_selected_oligos()
        if enableRedo:
            # If A LOT of oligos are selected, this could add considerable overhead.
            # (There will be one undo command in the undo stack for EACH oligo.)
            for oligo in selectedOs:
                oligo.applyColor(color)
        else:
            for oligo in selectedOs:
                oligo.setColor(color) # setColor does not emit the
                oligo.oligoAppearanceChangedSignal(oligo)

    def get_stranditem_for_strand(strand):
        """
        Each stranditem has a ._modelStrand attribute.
        Stranditems are connected to the model strand via a StrandItemController,
        which just connects model strand and model oligo events to strand item slots.

        Hmm... VirtualHelixItem.strandAddedSlot() simply creates a
            StrandItem(strand, self, self._viewroot)
        where strand is model strand, self=virtualHelixItem, viewroot is ?
        but does not save any direct reference to this.

        pitm = w().pathroot.partItemsForPart() -> partItem.
        vhitm = pitm._virtualHelixItemList, getOrderedVirtualHelixList(), vhItemForVH(vhref)

        vhitem.childItems()
        """
        vhitem = vhi(strand.virtualHelix())
        strandItem = next(sI for sI in vhitem.childItems() if getattr(sI, '_modelStrand', None) == strand)
        return strandItem

    def ensure_strand_is_visible(strand):
        """
        Using QGraphicsView.centerOn (self, QPointF pos)
        derived as CustomQGraphicsView class, instanced as obj w().sliceGraphicsView and w().self.pathGraphicsView
        """
        si = get_stranditem_for_strand(strand)
        si.ensureVisible()      # doesn't work?
        # Alternatively, grab the graphicsView and use centerOn()
        pos = si.scenePos()     # better than .pos() ?
        #vr = si.viewroot()
        # For some reason, pos coordinates are currently negative floats;
        # centerOn expects positive integers.
        w().pathGraphicsView.centerOn(pos)
        # edit, probably use partItem, which shows the part in the path view:
        # partItem is showed on top of pathview, and there is a transform and a matrix between the two.
        # pi().rect() --> total partItem extend.
        #pi().
        # Question: when you "move around" with ctrl+drag, do you
        # 1) Move all elements within a fixed view?
        # 2) Move the view, keeping the items in place?
        # QGraphicsView.ScrollHandDrag      # ./views/customqgraphicsview.py:91, as dragMode(), adjusted with setDragMode
        # scene.sceneRect() -> sceene dimensions.

        # New attempt, inferred from UI keyboard/mouse events in customqgraphicsview.py:350-

        # if event.key() == Qt.Key_Up:
        #   self.sceneRootItem.translate(0,self.keyPanDeltaY())
        #pathview.sceneRootItem.translate(0,self.keyPanDeltaY())
        # (mousewheel does pathview.zoomIn/Out(0.03) )
        # self._key_mod = Qt.Key_Control
        # CustomQGraphicsView.zoomToFit() is also a good reference...

        # pathview == w().pathGraphicsView          (TRUE)  - The window widget displaying the path scene
        # pathview.sceneRootItem == si.viewroot()   (TRUE)  - ?
        # pathview.scene() == si.scene()            (TRUE)  - Scene is...?
        # pathview in si.scene().views()            (TRUE)  -

        # StrandItem inheritance:
        # - QGraphicsLineItem
        # --- QGraphicsItem         Creates a 2D item for a QGraphicsScene. http://qt-project.org/doc/qt-4.8/qgraphicsitem.html

        # QGraphicsScene

        # scene.sceneRect()         # Scene's Bounding Rectangle, the extend of the scene.

        # Pathview inheritance:
        # - CustomQGraphicsView         # cadnano graphicsview baseclass
        # --- QGraphicsView             # "The QGraphicsView class provides a widget for displaying the contents of a QGraphicsScene".
        # -----

        #                 placed on                     viewed with
        # QGraphicsItem  -----------> QGraphicsScene   -------------> QGraphicsView
        # StrandItem                  QGraphicsScene                  QCustomGraphicsView,  # cadnano classes
        # stranditem                  w().pathscene                   w().pathGraphicsView
        # where w() is a the DocumentWindow(QMainWindow) view.

        # See also:
        # - http://qt-project.org/doc/qt-4.8/graphicsview.html - background info/guide.

        # What is the rootItem objects, e.g. w().pathRoot pathview.pathrootitem.PathRootItem(QGraphicsRectItem)?
        # - It creates a pathview.partitem.PartItem(QGraphicsRectItem) when a signal is sent to its partAddedSlot
        # - Contains dicts for selection and filtering, e.g. self._strandItemSelectionGroup, self._vhiHSelectionGroup, self._selectionFilterDict
        # I guess it is sort of the "main" QGraphicsItem in the scene...

        # Approach
        # 1) Use si.scenePos or maybe si.transformation().m11() or something relative to vhi or something to get pos for stapleItem.
        # QGraphicsItem.scenePos() Returns the item's position in scene coordinates. This is equivalent to calling mapToScene(0, 0).
        # 2) Find the currently viewed center, using pathview.rect()
        #       edit: pathview.rect() and .pos() refers to the position of the pathview window within the documentwindow.
        #       pathview is a CustomQGraphicsView. You need the scene stuff, maybe?
        #       pathview.transform().m11() is changed upon zooming.



    ### Strand shortcuts ###


    # Regarding colors:
    # If you have a QColor object, use qcolorobj.name() to get a hex string representation. ("#cc7700")
    # Use QColor("#cc7700") to create a QColor obj.
    # color *strings* are used in the model domain (strand, oligo, etc),
    # while QColors are used in the View domain (StrandItem, etc).


    ### Strand item shortcuts ###

    # ensure visibility:
    # http://pyqt.sourceforge.net/Docs/PyQt4/qgraphicsitem.html

    ### Window shortcuts ###
    # w() = documentwindow

    def get_stranditemselectiongroup():
        # for self = views.pathview.pathselection.SelectionItemGroup(QGraphicsItemGroup)
        # self.childItems() ->
        return w().pathroot.strandItemSelectionGroup()

    # Window elements corresponding to the UI buttons:
    #<addaction name="actionPathSelect"/>
    #<addaction name="actionPathPencil"/>
    #<addaction name="actionPathBreak"/>
    #<addaction name="actionPathInsertion"/>
    #<addaction name="actionPathSkip"/>
    #<addaction name="actionPathPaint"/>
    #<addaction name="actionPathAddSeq"/>

    ## More oligo path/color related:
    # w().pathColorPanel    # color selection. See also # w().palette()
    # w().pathGraphics      # PathView
    # w().pathToolManager   # Tool manager, including paintTool, addSeqTool, breakTool, etc.
    # color = QColor(oligo.color()) #, _updateColor, stranditem.py:400

    # paintToolMousePress() # stranditem.py:400
    #   color = self.window().pathColorPanel.stapColorName()

    ## Other ##
    # ensureVisible() method on a QGraphicsItem (requires coordinates or similar)


    # Regarding views: From left to right,
    # sliceview = the end-on view of helices. Displays partitem, virtualhelixitem, etc.
    # pathview = side-ways view of each helix. Displays partitem, virtualhelixitems, stranditems and decorators.
    # solidview = 3D representation
    # documentview = the whole document view. Contains each of the above views, as well as "ToolManagers" for pathview and sliceview.
    # Each "view" also has a "scene" and "root".

    # The root keeps track of elements, and includes e.g. the selectionGroups, available with
    # strandItemSelectionGroup() --> returns selected stranditems.



    def get_current_style_stap_color():
        """ Returns the currently selected staple 'PaintTool' color (as hex string) """
        w().pathColorPanel.stapColorName()

    def get_current_style_stap_color():
        """ Returns the currently selected scaffold 'PaintTool' color (as hex string) """
        w().pathColorPanel.scafColorName()

    ### Other ###
    def get_styles():
        """
        Returns the styles (currently in the form of a module).
        styles has information on saved colors for staples and scaffold, e.g.
            styles.stapColors, styles.scafColors lists.
        which are cycled when changing colors.
        """
        from views import styles
        return styles


    ### Document controller shortcuts ###

    def get_filename():
        """ Returns the full path to the file, e.g. "/home/you/cadnano_designs/HB24.json" """
        return dc().filename()

    def get_doctitle():
        """ Document title (file basename), e.g. "HB24.json" """
        return dc().documentTitle()


    def open_document(filepath=None):
        if filepath:
            dc().openAfterMaybeSaveCallback(filepath)
        else:
            #dc().openAfterMaybeSave()
            dc().actionOpenSlot()

    def save_document(filepath):
        dc().writeDocumentToFile(filepath)


    def get_fileopendir():
        """
        Returns the document controller's "fileopen dir", i.e. the directory it looks
        in when opening a new file.
        """
        return str(dc()._fileOpenPath)

    def set_fileopendir(dirpath, saveToSettins=False):
        """
        Sets the document controller's "fileopen dir", i.e. the directory it looks
        in when opening a new file.
        """
        if saveToSettins:
            dc()._writeFileOpenPath(dirpath)
        else:
            dc()._fileOpenPath = dirpath


    def enableAutocomplete(ns=None):
        """
        Enables tab-based autocomplete. The readline module must be available.
            <ns> is the namespace which readline starts out with.
            This should generally be the same as your interpreter uses,
            but defaults to globals() if ns is not provided.
        If you need to change the namespace at a later point, simply
        set the completer manually with:
            import readline, rlcompleter
            readline.set_completer(rlcompleter.Completer(ns).complete)
        """
        if ns is None:
            ns = globals()
        if readline:
            readline.set_completer(rlcompleter.Completer(ns).complete)
            readline.parse_and_bind("tab: complete")
        else:
            print "readline module not available. Must be installed for tab-based autocomplete to work. Google it."

    def ps(obj):
        """ Prints source-code for object/class/module <obj>. """
        # Yes, I use this that frequently!
        print inspect.getsource(obj)


    return locals()
