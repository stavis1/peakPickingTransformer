#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:05:23 2024

@author: 4vt
"""

import sys
from dataclasses import dataclass

#The dataclass decorator automatically adds several methods including __init__
#The slots parameter makes attribute access slightly faster.
@dataclass(slots = True)
class ms1_peak():
    '''This class holds the information about a single MS1 peak.'''
    mz: float
    rt: float
    intensity: float
    scan: int
    psm: int = -1
    vector: list = []

    def preprocess(self):
        '''
        Encodes the MS1 peak data as a vector for use by the transformer model.
        
        arguments:
            None
        returns:
            A list consisting of concatenated positional encodings for mz, rt, and intensity plus the psm number
        side effects:
            The .vector attribute gets defined if it was previously empty.   
        
        A -1 for the psm attribute means no psm is attached to this MS1 peak.
        Any other value should be the positive hash of the peptidoform
        '''
        if self.vector:
            return self.vector
        else:
            pass #TO DO

@dataclass(slots = True)
class PSM():
    '''This class holds the information about a single peptide-spectrum match event.'''
    mz: float
    rt: float
    charge: int
    peptidoform: str
    
    def peptidoform_hash(self):
        '''
        Calculates a positive hash of the peptidoform sequence.
        
        arguments:
            None
        returns:
            a positive integer
        side effects:
            None
        '''
        return hash(self.peptidoform) % 2**sys.hash_info.width


