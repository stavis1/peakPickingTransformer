#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:14:54 2024

@author: 4vt
"""

import setuptools

setuptools.setup(name="peakPickingTransformer",
                 version="0.0.0",
                 url="https://github.com/stavis1/peakPickingTransformer",
                 author="Steven Tavis, Andrew Willems",
                 author_email="stavis@vols.utk.edu, awillems@vols.utk.edu",
                 package_dir={"": "src"},
                 packages=setuptools.find_namespace_packages(where="src"),
                 include_package_data=True,
                 license_files=['LICENSE'],
                 classifiers=['License :: OSI Approved :: MIT License',
                              'Programming Language :: Python :: 3.12'],
                 python_requires='==3.12.4')

