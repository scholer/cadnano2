#!/usr/bin/env python
# encoding: utf-8

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
main.py

Created by Shawn Douglas on 2010-09-26.
"""

import sys
import os
sys.path.insert(0, '.')
# The above only adds the user's current working directory to the system path.
# If cadnano is called from a foreign directory which is it self a python module,
# i.e. the cwd contains a __init__.py file and a views/ folder, calling cadnano
# from this folder will cause an error, because cadnano cannot find e.g.
# the views/preferences.py module (because it is looking in <foreign dir>/views/
# This will make sure the base cadnano directory is the first in the system path.
# We use os.path.realpath in case this script is called as a symbolic link
# not residing in the actual cadnano directory, but e.g. in /usr/bin/
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))


import cadnano

if "-t" in sys.argv:
    os.environ['CADNANO_IGNORE_ENV_VARS_EXCEPT_FOR_ME'] = 'YES'

if "-p" not in sys.argv:
    # Having our own NSApplication doesn't play nice with
    # collecting profile data.
    try:
        # If we are in Mac OS X, initialize Mac OS X specific stuff
        supportsPythonObjCBridge = False
        import objc
        supportsPythonObjCBridge = True
    except Exception, e:
        print "Not on MAC:", e
    if supportsPythonObjCBridge:
        pass
        from osx.CNApplicationDelegate import sharedDelegate as appDelegate
    # else:
    #     from applicationdelegate import ApplicationDelegate



if __name__ == '__main__':
    cadnano.initAppWithGui()
    app = cadnano.app()
    if "-p" in sys.argv:
        print "Collecting profile data into cadnano.profile"
        import cProfile
        cProfile.run('app.exec_()', 'cadnano.profile')
        print "Done collecting profile data. Use -P to print it out."
        exit()
    elif "-P" in sys.argv:
        from pstats import Stats
        s = Stats('cadnano.profile')
        print "Internal Time Top 10:"
        s.sort_stats('cumulative').print_stats(10)
        print ""
        print "Total Time Top 10:"
        s.sort_stats('time').print_stats(10)
        exit()
    elif "-t" in sys.argv:
        print "running tests"
        from tests.runall import main as runTests
        runTests(useXMLRunner=False)
        exit()
    app.exec_()
