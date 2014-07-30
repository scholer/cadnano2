#!/usr/bin/env python
# encoding: utf-8
# The MIT License
#
# Copyright (c) 2014 Wyss Institute at Harvard University, Rasmus Sorensen
#
"""
This module (package) uses the __path__ variable to load PySide or PyQt UI widgets,
depending on which is loaded/available.

The __path__ variable is a list of locations (paths) where the interpreter should
look for files. This is calculated and set dynamically on first import.
This means that if you are in the cadnano root directory you get this:
>>> import model; print model.__path__
['model']  # the 'model' directory in the <cadnano-root> folder
Whereas if you are in an unrelated path, you get:
>>> import model; print model.__path__
['<path-to-cadnano-root-dir>/model']  # the full path to the 'model' directory in the <cadnano-root> folder

"""

import os
import util
qt_available = util.chosenQtFramework or util.find_available_qt_framework()
qt = qt_available.lower()


if qt == 'pyqt4':
    print "PyQt4 UI widgets should be picked up automatically through the package structure."
elif qt == 'pyside':
    # Setting __path__ like this should make python look in pyside_ui/ for submodules:
    #old_path = __path__
    __path__ = [os.path.join(__path__[0], 'pyside_ui')]
    #print "Modified ui module to use path: ", __path__, "(original path was: ", old_path, ")"
else:
    print "WARNING, no PyQt4 or PySide! - Cadnano UI will not be available."
