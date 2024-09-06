#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:10:28 2024

@author: anon
"""

import unittest
#unittest will run any test suite that is in the global namespace
#so either import the whole file or directly name the test suites you want to run
from argument_parser_tests import parserTestSuite

if __name__ == '__main__':
    unittest.main()
