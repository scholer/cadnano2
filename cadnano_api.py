# The MIT License
#
# Copyright (c) 2013 Wyss Institute at Harvard University
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

# pylint: disable-msg=W0212

"""

"API" - a series of shortcuts meant to be made available to the user,
e.g. through the interactive prompt inside cadnano.

These shortcut-functions makes it considerably more comfortable to
use the interactive prompt, and provides a range of features not
directly available from cadnano's UI.

The functions herein also serve as a reference on how to use
cadnano's object model programatically.

Feel free to add the code you use the most as a function to this module!


@authors: Rasmus Scholer Sorensen,

"""

import re
import inspect
from collections import deque

try:
    import readline
    import rlcompleter
except ImportError:
    readline = None

import cadnano
import util

util.qtWrapImport('QtGui', globals(),  ['QTransform'])
util.qtWrapImport('QtCore', globals(),  ['QPropertyAnimation', 'pyqtProperty', 'QObject', 'QEasingCurve'])



#### Constants / settings for API functions #####

ANIMATE_DURATION_MSEC = 500
ANIMATE_ENABLED_DEFAULT = True

# PySide QEasingCurve is NOT instantiated with an integer, but takes a QtCore.Type instance.
ANIMATE_EASINGCURVE = QEasingCurve.Linear # This should work for both PyQt4 and PySide and is also more readable.
# http://qt-project.org/doc/qt-4.8/qeasingcurve.html

# The last animation and transform_adaptor (for PySide) must be captured,
# otherwise they are garbage-collected before the animation completes.
# However, I'm not sure if I just have to save the last ones or more. Using a deque with maxlen=5 for now...
animators = deque(maxlen=5) # [None]
transform_adaptors = deque(maxlen=5) # [None]
# (last_selected_strand, current_follow_strand)
current_follow_strand_tuple = [(None, None)]


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

def get_api(app=None):
    """
    Returns a namespace dict using app as base.
    <app> should be a cadnano app. If app=None, tries to import cadnano module and use cadnano.app().

    A convenient way to invoke this is:
    locals().update(cadnano_api.get_api(a()))

    If you need to reload the api module:
        reload(cadnano_api)
    or just exec the with:
        execfile('cadnano_api.py')
    followed by:
        locals().update(get_api(a()))
    """
    # This needs to be split out to separate module if you want to use cadnano.app()
    # You cannot import cadnano in this module, since that would create cyclic import.
    #if app is None:
    #    app = cadnano.app() # App singleton
    # locals() are the local variables, available only from within this function (i.e. defined here).
    # globals() are all the variables that is accessible from here, but which were not defined here.
    # return {k : v for k, v in globals().items() if k[0] != '_'}
    # Dict comprehensions is not compatible with Maya2012's python2.6, so falling back to :
    return dict((k, v) for k, v in globals().items() if k[0] != '_')


### Basic cadnano object shortcuts ###

def a():
    """ Return main cadnano app object. """
    return cadnano.app()
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
def pathview():
    """
    Returns the documentwindow's QGraphicsView pathview, displaying the scene.
    For slice view, use w().sliceGraphicsView
    """
    return w().pathGraphicsView
def pathscene():
    """
    Returns the documentwindow's QGraphicScene path scene.
    For slice scene, use w().slicescene
    """
    return w().pathscene
def pathroot():
    """
    Returns the root QGraphicsRectItem object for the path scene documentwindow's path scene.
    For slice root, use w().sliceroot
    """
    return w().pathroot
def first(seq, fallback=None):
    """
    Return the first encountered element in seq.
    If seq is unordered (e.g. a map), returns an arbitrary element, without removing it.
    Note: In many cases, you can just as easy use .pop() if you are not worried about the
    rest of the set/sequence.
    """
    return next(iter(seq), fallback)



### Strand shortcuts

def get_selected_strands():
    selectedStrands = set(strand for strandSet, strands in d().selectionDict().items() for strand in strands)
    return selectedStrands

def get_first_selected_strand():
    return first(get_selected_strands())

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
    #selectedOs = {strand.oligo() for strandSet, strands in d().selectionDict().items() for strand in strands}
    # Set comprehensions are also not supported by Maya2012's python2.6, :
    selectedOs = set(strand.oligo() for strandSet, strands in d().selectionDict().items() for strand in strands)
    return selectedOs


def get_oligo_colors():
    """
    Returns a set of colors used by the currently selected oligos.
    """
    return set(oligo.color() for oligo in get_selected_oligos())


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
        util.qtWrapImport('QtCore', globals(), ['QString'])
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

def parse_locstring(oligo_locstring):
    # Oligos are often represented by oligo.locString() which returns <vHelixIndex>[<5pIndex>]
    pat = re.compile(r'(\d*)\[(\d*)\](-.*)?')
    match = pat.match(oligo_locstring)
    if match:
        return [int(g) for g in match.groups()[0:2]]
    else:
        return match, None

def get_oligo_from_locstring(oligo_locstring):
    """
    Get oligo object from string '59[63]'.
    Useful as:
        centerOnStrand(get_oligo_from_locstring(<loc string>).strand5p())
    See also:
        get_strand_from_locstring(locstring)
    """
    strand = get_strand_from_locstring(oligo_locstring)
    if not strand:
        print "Strand not found: ", strand
        return
    return strand.oligo()

def get_strand_from_locstring(locstring):
    """
    Get strand object from string '59[63]'.
    """
    hi, si = parse_locstring(locstring)
    if not hi or not si:
        print "parse_locstring(%s) returned %s, aborting!" % (locstring, (hi, si))
        return
    #else:
    #    print "parse_locstring(%s) returned %s, looks good." % (locstring, (hi, si))
    helix = vh(hi)
    #print "Helix is: ", helix
    # Assume the oligo is a staple strand:
    strand = next((strand for strand in helix.stapleStrandSet() if strand.idx5Prime()==si), None)
    if not strand:
        print "Staple not found on staplestrandset, searching scaffoldStrandSet..."
        strand = next((strand for strand in helix.scaffoldStrandSet() if strand.idx5Prime()==si), None)
    return strand



### STRAND ITEM FUNCTIONS ###

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
    # When a strand is selected, it is REMOVED from vhitem.childItems() ??
    # When deselected, the strand is included in vhitem.childItems() again ??
    # StrandItem.PathRootItem.SelectionItemGroup(QGraphicsItemGroup).addToGroup method
    # strandItem._viewroot.strandItemSelectionGroup().addToGroup(strandItem)
    #   "Adds the given item and item's child items to this item group.
    #   The item and child items will be reparented to this group,
    #   but its position and transformation relative to the scene will stay intact."
    # So... it is probably this re-parenting which does it.
    # Which just means that you should grab stranditem from the viewroot.strandItemSelectionGroup() instead.
    vhitem = vhi(strand.virtualHelix())
    try:
        strandItem = next(item for item in vhitem.childItems() if getattr(item, '_modelStrand', None) == strand)
    except StopIteration:
        sisg = vhitem.viewroot().strandItemSelectionGroup()
        strandItem = next((item for item in sisg.childItems() if getattr(item, '_modelStrand', None) == strand), None)
    # Alternatively, you could search for the strand item in the list of path scene items:
    # strandItem = next((item for item in pathscene().items() if getattr(item, '_modelStrand', None) == strand), None)
    return strandItem

def get_selected_stranditems():
    """
    Returns selected StrandItems in the path view.
    """
    sisg = pathroot().strandItemSelectionGroup()    # This includes both StrandItems as well as caps, xovers, etc.
    # Alternatively, you could use pathscene().selectedItems()  # would return all selected items, not just strand-related.
    stranditems = [item for item in sisg.childItems() if hasattr(item, '_modelStrand')]
    return stranditems

def get_first_selected_item(key=None):
    """ Returns an arbitrary selected item from the path view. """
    candidates = pathroot().strandItemSelectionGroup().childItems()
    if key:
        it = (item for item in candidates if key(item))
    else:
        it = iter(candidates)
    return next(it, None)


def linecenter(qLine):
    """ Calculate the center point of a line. """
    x1, y1 = qLine.x1(), qLine.y1()
    x2, y2 = qLine.x2(), qLine.y2()
    return ((x1+x2)/2.0, (y1+y2)/2.0)

def getRealItemScenePos(item):
    """
    Returns item's real position in scene space. Mostly for e.g. stranditems.
    This will change as the root item is moved round the scene,
    but should not change when zooming.
    """
    view = pathview()
    try:
        vhitem = item.virtualHelixItem()
        linepos = linecenter(item.line()) # StrandItem lines are drawn in the virtual-helix space.
    except AttributeError:
        # E.g. EndPointItems, caps, etc, has no VhItem, position should be in scene coordinates:
        return item.scenePos()
    # Should I map to scene space or maybe use pathrootitem, i.e. vhitem.mapToItem(pathroot(), *linepos) ?
    # mapping to pathroot produces constant result independent of zoom and transform.
    # mapping to scene produces variable results.
    return vhitem.mapToScene(*linepos)

def getViewCenterPos(relativeToItem=None):
    """
    Returns QPointF with the view's center in scene space.
    """
    view = pathview()
    if relativeToItem is None:
        return view.mapToScene(view.rect().center())
    else:
        return view.mapToItem(relativeToItem, view.rect().center())


class TranslationAdaptor(QObject):
    def __init__(self, parent, object_to_animate, dx, dy):
        """
        Default constructor
        """
        super(TranslationAdaptor, self).__init__() # Invoke QObject init
        self.object_to_animate = object_to_animate
        self.t0 = t0 = object_to_animate.transform()
        self.x0 = t0.dx()
        self.y0 = t0.dy()
        self.dx = dx
        self.dy = dy
        self._progress = 0.0

    def getNewTransform(self, progress):
        return self.t0.fromTranslate(self.x0+self.dx*progress,
                                     self.y0+self.dy*progress)

    def _getProgress(self):
        return self._progress
    def _setProgress(self, progress):
        """ Value is percentage of total move, from 0..1 """
        #progress = p.x()
        tnew = self.getNewTransform(progress)       # Create a new transform based on 'progress' value
        self.object_to_animate.setTransform(tnew)   # Set object's transform.
        self._progress = progress
        print "Progress: %s, dx(), dy(): %s" % (progress, (self.object_to_animate.transform().dx(), self.object_to_animate.transform().dy()))
    Progress = pyqtProperty(float, _getProgress, _setProgress)


def animate_translate(item, dx, dy, msec=ANIMATE_DURATION_MSEC):
    """
    If you move an item in a single translation, it can sometimes be hard to
    follow with your eyes.
    Translating in steps might help.
    This uses deprecated QGraphicsItemAnimation
    """
    # based on http://engineersjourney.wordpress.com/2012/09/05/pyqt-and-animating-qgraphicsitem-objects/
    # see also: https://github.com/Werkov/PyQt4/tree/master/examples/animation
    #try:
    #    from PyQt4.QtGui import QTransform
    #    from PyQt4.QtCore import QPropertyAnimation, pyqtProperty, QObject, QEasingCurve
    #except ImportError:
    #    from PySide.QtGui import QTransform
    #    from PySide.QtCore import QPropertyAnimation, Property, QObject, QEasingCurve
    #    pyqtProperty = Property

    transform_adaptor = TranslationAdaptor(item, item, dx, dy)
    animation = QPropertyAnimation(transform_adaptor, 'Progress')
    animation.setDuration(msec)
    #t0 = item.transform()
    animation.setStartValue(0.0) # Start value of "Progress" property of transform_adaptor.
    #newx, newy = t0.dx(), t0.dy()
    #t1 = t0.fromTranslate(newx, newy)
    animation.setEndValue(1.0)  # End value of "Progress" property of transform_adaptor.
    #animation.setLoopCount(1) # 1 is default
    # EasingCurves: http://qt-project.org/doc/qt-4.8/qeasingcurve.html
    animation.setEasingCurve(QEasingCurve(ANIMATE_EASINGCURVE))

    print "Starting animation..."
    animation.start()
    print "Moved dx=%s, dy=%s." % (dx, dy)
    #transform_adaptors[0] = transform_adaptor
    #animators[0] = animation
    transform_adaptors.append(transform_adaptor)
    animators.append(animation)
    # You MUST capture this, or it will be garbage-collected!
    # Edit: For PySide, it seems you must also capture the transform_adaptor object,
    # or it too will be GC'ed.
    return animation


def centerOnScenePos(point, animate=True):
    """
    Translate scene root item so point is at the center of the pathview.
    """
    if animate is None:
        animate = ANIMATE_ENABLED_DEFAULT
    # calculate translation:
    viewcenterpos = getViewCenterPos()
    dx = viewcenterpos.x() - point.x()
    dy = viewcenterpos.y() - point.y()
    root = pathroot()
    # Translate root item (tranlating the view doesn't work, unfortunately...)
    #print "Scene pos before translating: view=%s, strand=%s" % (viewcenterpos, strandpos)
    if animate:
        animator = animate_translate(root, dx, dy)
        if animator not in animators:
            animators.append(animator)
        # You can use animation.finished.connect(self.remove_finished_animation)
        # To invoke a callback.
        # Alternative way to translate:
        # pr.setTransform(pr.transform().fromTranslate(dx, dy))
    else:
        root.translate(dx, dy)
        animator = None
    #print "New scene pos: view=%s, strand=%s" % (getViewCenterPos(), getRealItemScenePos(si))
    return animator



def centerOnSelected(key=None, animate=None):
    """
    Center on selected item. If more items are selected, will pick an arbitrary item.
        key :       A key function which can be used to filter the the list of selected items.
        animate:    Whether to animate the movement (True/False/None). If None, will use the default
                    specified by ANIMATE_ENABLED_DEFAULT variable.

    Update: Using centerOnScenePos rather than pathview().centerOn(...).
    """
    item = get_first_selected_item(key)
    if not item:
        print "No item selected, aborting..."
        return
    # if item is a strandItem, then its scenePos will be that of its helix.
    # If it on the other hand is an endpoint or similar, then it seems to be ok.
    # Edit: Actually, it they might be equivalent.
    # The difference migth be if the parent pos changes.
    # AND, UPON SELECTION, AN ITEM IS RE-PARENTED TO THE SELECTION GROUP!!
    #try:
    #    vhitem = item.virtualHelixItem()
    #except AttributeError:
    #    # E.g. EndPointItems, caps, etc, has no VhItem, position should be in scene coordinates:
    #    pathview().centerOn(item.scenePos())
    #else:
    #    # Transform the item
    #    pathview().centerOn(vhitem.mapToScene(*linecenter(item.line())))
    scenepos = getRealItemScenePos(item)
    animator = centerOnScenePos(scenepos, animate=animate)
    return animator



def centerOnStrand(strand=None, animate=True):
    """
    Note: Animate doesn't work. It proved more troublesome than I had first imagined...

    Using QGraphicsView.centerOn (self, QPointF pos)
    derived as CustomQGraphicsView class, instanced as obj w().sliceGraphicsView and w().self.pathGraphicsView

    About the QGraphicsScene--QGraphicsView architecture:

                      placed on                     viewed with
     QGraphicsItem  -----------> QGraphicsScene   -------------> QGraphicsView
     StrandItem                  QGraphicsScene                  QCustomGraphicsView,  # cadnano classes
     stranditem                  w().pathscene                   w().pathGraphicsView
     where w() is a the DocumentWindow(QMainWindow) view.

     See also:
     - http://qt-project.org/doc/qt-4.8/graphicsview.html - background info/guide.

     What is the rootItem objects, e.g. w().pathRoot pathview.pathrootitem.PathRootItem(QGraphicsRectItem)?
     - It creates a pathview.partitem.PartItem(QGraphicsRectItem) when a signal is sent to its partAddedSlot
     - Contains dicts for selection and filtering, e.g. self._strandItemSelectionGroup, self._vhiHSelectionGroup, self._selectionFilterDict
     I guess it is sort of the "main" QGraphicsItem in the scene...

     cadnano access:
     pathview == w().pathGraphicsView          (TRUE)  - The window widget displaying the path scene
     pathview.scene() == si.scene()            (TRUE)  - Scene is...?
     pathview.sceneRootItem == si.viewroot()   (TRUE)  - ?
     pathview in si.scene().views()            (TRUE)

     StrandItem inheritance:
     - QGraphicsLineItem
     --- QGraphicsItem         Creates a 2D item for a QGraphicsScene. http://qt-project.org/doc/qt-4.8/qgraphicsitem.html

     QGraphicsScene
     scene.sceneRect()         # Scene's Bounding Rectangle, the extend of the scene.
     Scene does not seem to contain much useful methods; mostly just event stuff.

     Pathview inheritance:
     - CustomQGraphicsView         # cadnano graphicsview baseclass
     --- QGraphicsView             # "The QGraphicsView class provides a widget for displaying the contents of a QGraphicsScene".

    Other COTCHA's:
    - si.ensureVisible()      # doesn't work  -- that ensureVisible is for standard widgets I think.
    - pathroot.moveBy(dx, dy) # Uses the pos() coordinate system.

Old comments:

    # Approach
    # 1) Use si.scenePos or maybe si.transformation().m11() or something relative to vhi or something to get pos for stapleItem.
    # QGraphicsItem.scenePos() Returns the item's position in scene coordinates. This is equivalent to calling mapToScene(0, 0).
    # 2) Find the currently viewed center, using pathview.rect()
    #       edit: pathview.rect() and .pos() refers to the position of the pathview window within the documentwindow.
    #       pathview is a CustomQGraphicsView. You need the scene stuff, maybe?
    #       pathview.transform().m11() is changed upon zooming.
    # w().pathGraphicsView.centerOn(pos)  # would not work, you are centering the whole document window.
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
    # It would seem that in cadnano, the scene root item is translated (rather than "moving the view") ?
    # if event.key() == Qt.Key_Up:
    #   self.sceneRootItem.translate(0,self.keyPanDeltaY())
    #pathview.sceneRootItem.translate(0,self.keyPanDeltaY())
    # (mousewheel does pathview.zoomIn/Out(0.03) )
    # self._key_mod = Qt.Key_Control
    # CustomQGraphicsView.zoomToFit() is also a good reference...

    # THIS MEANS THAT AS YOU MOVE AROUND IN CADNANO, THE ITEMS' SCENE COORDINATES CONSTANTLY CHANGE!
    # (Not if you scale, though, only when you move.)


    si = get_stranditem_for_strand(strand)
    root = si.viewroot()      # Root ITEM in the scene. Parent for all other graphics items.
    view = pathview()

    # Maybe grab the graphicsView and use centerOn() ?

    #scenepos = si.scenePos()     # si.pos() refers to "window" coordinates, which makes little sense to use.
    # scenePos() returns a constant x-coordinate, which I belive is the virtualhelix coordinate.
    # in fact, both coordinates (x and y) are the same as virtualhelixitem.scenePos.
    # Where, relative to the helix, the stranditem is drawn is controlled by the line arguments:

    strandhelixpos = linecenter(si.line()) #
    print "strandhelixpos = %s, si.scenePos = %s" % (strandhelixpos, si.scenePos())
    vhitem = si.virtualHelixItem()
    # The floats are: x1, y1, x2, y2, where line goes from p1=(x1, y1) to p2=(x2,y2).
    # These floats are in the vhitem space. The line does not have any transformation on its own.
    # So, to translate:

    # Line                      vhItem
    # vhi space                 scene space             documentwindow space
    #          vhi.mapToScene            view.mapFromScene
    # linepos  ---------------> scenepos --------------> viewpos

    # viewpos should be positive?
    strandscenepos = vhitem.mapToScene(*strandhelixpos)  # Returns QPointF
    strandviewpos = view.mapFromScene(strandscenepos)   # Returns QPoint (integers)
    print "strandscenepos = %s, strandviewpos = %s" % (strandscenepos, strandviewpos)

    # How to center on strand?
    #   A)  Use view.centerOn(pos)
    #   B)  Use view.translate(x, y) - you have to calculate from something?
    #   C)  Translate the root item with sceneRootItem.translate(dx, dy)
    #        (this is how the CustomQGraphicsView mouse/keyboard moves around)

    # A) Regarding view.centerOn():
    # "Scrolls the contents of the viewport to ensure that the scene coordinate pos, is centered in the view."
    # However, for me it seems this doesn't really work. See the centerOnSelected() function.

    # B) Regarding view.translate(dx, dy) -- doesn't work, no update.

    # C) Regarding translating the root item:
    # Question: How do you calculate the view's position? Answer: See getViewCenterPos() function.

    # view.transform()  # changes when zooming, but not panning with mouse.
    # transform vs matrix:
    # matrix = 2-by-2, contains scale and ... rotation?
    # transform = 3-by-3, contains matrix and translation
    # There is a note on http://qt-project.org/doc/qt-4.8/qgraphicsview.html#translate that translate might not work.
    # This can allegedly be fixed by adding scrollbars to the view.
    #scrollbar = view.verticalScrollBar()
    #scrollbar.setValue(scrollbar.value()+30) # doesn't work.
    ## one-liner:
    #scpos = vhitem.mapToScene(*linecenter(next(iter(get_selected_stranditems())).line()))
    ## this work for the x-position, but not y/vertical (you also need to update vhitem...)
    #view.centerOn(vhitem.mapToScene(*linecenter(next(iter(get_selected_stranditems())).line())))
    # view.rect()       # QRect on the documentwindow.
    # view.sceneRect()  # scene rectangle. Does not change if panning or zooming.

    """

    if strand is None:
        strand = get_first_selected_strand()
        if strand is None:
            print "No strand selected, using last recorded selection:"
            strand = current_follow_strand_tuple[0][0] # either 0 or 1
    # get basic elements:
    si = get_stranditem_for_strand(strand)
    root = si.viewroot()      # Root ITEM in the scene. Parent for all other graphics items.
    view = pathview()

    # calculate translation:
    viewcenterpos = getViewCenterPos()
    strandpos = getRealItemScenePos(si)
    dx = viewcenterpos.x() - strandpos.x()
    dy = viewcenterpos.y() - strandpos.y()
    # Translate root item (tranlating the view doesn't work, unfortunately...)
    #print "Scene pos before translating: view=%s, strand=%s" % (viewcenterpos, strandpos)
    if animate:
        animator = animate_translate(root, dx, dy)
        if animator not in animators:
            animators.append(animator)
        # You can use animation.finished.connect(self.remove_finished_animation)
        # To invoke a callback.
        # Alternative way to translate:
        # pr.setTransform(pr.transform().fromTranslate(dx, dy))
    else:
        root.translate(dx, dy)
    #print "New scene pos: view=%s, strand=%s" % (getViewCenterPos(), getRealItemScenePos(si))
    return strand



def follow_strand(strand=None, direction='5p', stopAtEnd=True, animate=True):
    """
    See follow_strand_5p() doc.
    """
    selected_strand = None
    if strand is None:
        selected_strand = get_first_selected_strand()
        # (last_selected_strand, current_follow_strand)
        print "Selected strand: ", selected_strand
        print "current_follow_strand_tuple[0]: ", current_follow_strand_tuple[0]
        if selected_strand == current_follow_strand_tuple[0][0] or selected_strand is None:
            # If either no selection or selection haven't changed:
            strand = current_follow_strand_tuple[0][1] # Continue from the last saved strand.
        else:
            strand = selected_strand
    if strand is None:
        print "No strand specified and no strand selected, cannot center."
        return

    nextstrand = strand._strand5p if direction == '5p' else strand._strand3p
    print "following strand: %s -- to next strand --> %s" % (strand, nextstrand)

    if stopAtEnd and nextstrand is None:
        nextstrand = strand
    elif nextstrand is None:
        return nextstrand

    centerOnStrand(nextstrand, animate=animate)
    current_follow_strand_tuple[0] = (selected_strand, nextstrand)
    return nextstrand

def follow_strand_5p(strand=None, stopAtEnd=True, animate=True):
    """
    Follow strand in the 5p direction. If strand is none, use currently selected strand.
    Returns the newly focused strand.
    Use as:
        mystrand = follow_strand_5p()           # 1) uses the currently selected strand
        mystrand = follow_strand_5p(mystrand)   # 2) updates mystrand
        mystrand = follow_strand_5p(mystrand)   # 3) updates mystrand again.
        mystrand = follow_strand_3p(mystrand)   # 4) Goes back. mystrand should now be same as after step (2).
    If stopAtEnd is True, will NOT go further, will just focus on current strand and return current strand.
    """
    return follow_strand(strand=strand, direction='5p', stopAtEnd=stopAtEnd, animate=animate)

def follow_strand_3p(strand=None, stopAtEnd=True, animate=True):
    """
    See follow_strand_5p() doc.
    """
    return follow_strand(strand=strand, direction='3p', stopAtEnd=stopAtEnd, animate=animate)


def zoomIn(relative=None, absolute=None):
    """
    Zoom In (pathview).
    If absolute is specified, zoom to an absolute zoom level.
    Else, zoom in (scale) using relative.
    """
    if absolute:
        w().pathGraphicsView.zoomIn(absolute)
        return
    if relative is None:
        relative = 1.2
    w().pathGraphicsView.scale(relative, relative)

def zoomOut(relative=None, absolute=None):
    """
    Zoom Out (in the pathview).
    If absolute is specified, zoom to an absolute zoom level.
    Else, zoom in (scale) using relative.
    """
    if absolute:
        w().pathGraphicsView.zoomOut(absolute)
        return
    if relative is None:
        relative = 1.2
    w().pathGraphicsView.scale(1.0/relative, 1.0/relative)



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

def get_current_style_scaf_color():
    """ Returns the currently selected scaffold 'PaintTool' color (as hex string) """
    w().pathColorPanel.scafColorName()




## Part shortcuts ##

def get_active_baseIndex():
    """ Returns the active baseindex (usually adjusted by the "slider"). """
    return p().activeBaseIndex()

def set_active_baseindex(index):
    """ Sets the active baseindex (usually adjusted by the "slider"). """
    p().setActiveBaseIndex(index)

def move_active_baseindex_to_strand(strand=None, idx_point='mid'):
    """
    Moves the active baseindex (and slider) to the mid-point of the specified strand.
    If no strand is provided, this will use the currently selected strand, if any.
    idx_point can be any of:
        'mid'   : midpoint of the strand (default)
        'high'  : high base idx (right-most)
        'low'   : low base idx (left-most)
        '3p'  : 3-prime end of strand
        '5p'  : 5-prime end of strand
    Returns (for convenience):
        (<strand used>, base_idx)
    """
    if strand is None:
        strand = first(get_selected_strands())
    if not strand:
        print "No strand selected, no strand provided."
        return
    if idx_point == 'high':
        idx = strand.highIdx()
    elif idx_point == 'low':
        idx = strand.lowIdx()
    elif idx_point == '3p':
        idx = strand.idx3Prime()
    elif idx_point == '5p':
        idx = strand.idx5Prime()
    else:
        idx = sum(strand.idxs())/2
    set_active_baseindex(idx)
    return strand


def get_staplesequences():
    p().getStapleSequences()


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
