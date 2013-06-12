#!/usr/bin/env python
# -*- coding: utf-8 -*-
##    Copyright 2011 Rasmus Scholer Sorensen, rasmusscholer@gmail.com
## 
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Created on Sat Apr 20 2013

@author: scholer

"""

import os
import util, cadnano
from model.strandset import StrandSet
from model.enum import StrandType
from model.parts.part import Part
from model.oligo import Oligo

from helpcompatibleobject import HelpCompatibleObject

#try:
#    import IPython
#    ipythonimported = True
#except:
#    ipythonimported = False


cadnano_console_path = os.getcwd()
if not "cadnano_console" in cadnano_console_path:
    cadnano_console_path +=  "/plugins/cadnano_console"


class CadnanoAPI(HelpCompatibleObject):
    """
    Application programming interface for cadnano2.
    Not really implemented yet, feel free to contribute.
    All contributed methods should add a description to the help variable.
    Help can be added in three ways:
    1) Ammend the _helpstr via the addHelpStr(str) method
    2) Append the helpitems list with a two-tuple containing (header, helptext)
    3) Place a text file in the 'help' directory.
    """

    def __init__(self):
        #self.__super__.__init__()
        self.config = dict()


    def app(self):
        return cadnano.app()

    def docctrl(self):
        try:
            return list(self.app().documentControllers())[0]
        except:
            return None

    def doc():
        return self.docctrl().document()

    def filename():
        return self.docctrl().filename()
    
    def doctitle():
        return self.docctrl.documentTitle()

    def colorSelected(color=None):
        prefkey = 'colorSelected'
        if color:
            self.config[prefkey] = color
        elif self.config[prefkey]:
            color = self.config[prefkey]
        else:
            print "No color in use."
            return
        

    def selectedOligosReal(self):
        """ Return oligos actually selected (not all on helix like cadnano2 does).
        """
        doc = self.doc()
        sDict = self.doc().selectionDict()
        selectedOs = set()
        for sS in sDict.iterkeys():
            for strand in sS:
                 selectedOs.add(strand.oligo())
            # end for
        # end for
        return selectedOs if len(selectedOs) > 0 else None
    #end def
        # self.doc().selectionDict() # This is referred to with a strandset object.


    def getInitialHelpStr(self):
        helpstr = """
Help for the Cadnano console and API:

In general, parts are the component you generally want to use.
Active part is available via api.part(), and all oligos for 
that part are available via part.oligos() 
Selections are done at the document level, i.e. doc.selectedOligos(), 
doc.getSelectedValue(), doc.getSelectedStrandValue
Use [elem for elem in dir(doc) if "sel" in elem.lower()] to see all.

"""
