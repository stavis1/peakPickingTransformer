#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:27:02 2024

@author: 4vt
"""

import unittest
from copy import copy
import sys

from peakPickingTransformer.argument_parser import Args, ArgumentError

class parserTestSuite(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        #super() accesses the parent class methods so we can run unittest.TestCase's init procedure
        super().__init__(*args, **kwargs)

        #we want to make sure we don't perminantly modify command line parameters
        #so we'll store them in this variable for the duration of each test case
        self.initargs = copy(sys.argv)
    
    def tearDown(self, *args, **kwargs):
        super().tearDown(*args, **kwargs)
        
        #we replace the modified sys.argv with its initial state
        sys.argv = copy(self.initargs)
        
    def testExceptionRaisedOnMissingParam(self):
        sys.argv = [sys.argv[0]] + '--task train'.split()
        with self.assertRaises(ArgumentError):
            args = Args()

    def testNoExceptionRasiedOnCompleteParams(self):
        sys.argv = [sys.argv[0]] + '--task train --output example'.split()
        try:
            args = Args()
        except ArgumentError:
            self.assertTrue(False, msg = 'An exception was inappropriately raised for present params')            
            
    def testExceptionRaisedOnMissingFile(self):
        sys.argv = [sys.argv[0]] + '--task infer --output example --mzml missing --psms missing --model missing'.split()
        with self.assertRaises(ArgumentError):
            args = Args()

    def testNoExceptionRasiedOnExtantFiles(self):
        sys.argv = [sys.argv[0]] + f'--task infer --output test --mzml {__file__} --psms {__file__} --model {__file__}'.split()
        try:
            args = Args()
        except ArgumentError:
            self.assertTrue(False, msg = 'An exception was inappropriately raised for extant files')            

#this allows us to run only the tests in this file
if __name__ == '__main__':
    unittest.main()
