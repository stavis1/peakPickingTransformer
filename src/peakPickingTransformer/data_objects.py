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
    label = -1
    vector: list = []

    def __hash__(self):
        '''
        Hashes the uniquely identifying information about an MS1 peak.
        '''
        return hash((self.scan, self.mz))

    def preprocess(self):
        '''
        Encode the MS1 peak data as a vector for use by the transformer model.
        
        arguments:
            None
        returns:
            A list consisting of concatenated positional encodings for mz, rt, and intensity plus the psm number
        side effects:
            The .vector attribute gets defined if it was previously empty.   
        
        A -1 for the psm attribute means no psm is attached to this MS1 peak.
        Any other value should be the positive hash of the peptidoform.
        A -1 for the Y attribute means that the peak is not labeled.
        Any other value should be the positive has of the feature this peak belongs to.
        '''
        raise NotImplementedError()
    
    def set_label(self, peptidoform, charge):
        '''
        Calculate a positive hash of the feature this MS1 peak belongs to.
        
        arguments:
            peptidoform: The modified peptide sequence of the feature.
            charge: The charge state of the feature.
        returns:
            None
        side effects:
            Sets the label attribute to the positive hash of the feature.
        '''
        self.label = hash((peptidoform, charge)) % 2**sys.hash_info.width

@dataclass(slots = True)
class PSM():
    '''This class holds the information about a single peptide-spectrum match event.'''
    mz: float
    rt: float
    charge: int
    peptidoform: str
    
    def peptidoform_hash(self):
        '''
        Calculate a positive hash of the peptidoform sequence.
        
        arguments:
            None
        returns:
            a positive integer
        side effects:
            None
        '''
        return hash(self.peptidoform) % 2**sys.hash_info.width

class Feature:
    '''This class holds all information about a combination of peptidoform and charge state'''
    def __init__(self, sequence, charge):
        '''
        Iniitalize the feature object with minimal information.
        
        arguments:
            sequence: The peptidoform sequence, with modificaitons.
            charge: The charge state of the peptidoform.
        returns:
            None
        side effects:
            Initialize the peptidoform and charge attributes.
        
        Implementaton note: this should be called by a keydefaultdict while parsing the PSM table.
        '''
        self.peptidoform = sequence
        self.charge = charge
        self.psms = []
        self.ms1s = [] #this will be a list of lists where each sublist contains a single XIC's set of MS1 peaks
        self.xic_peaks = []
    
    def add_psm(self, psm):
        '''
        Add a PSM object to the PSM list for a feature.
        
        arguments:
            psm: A PSM object.
        returns:
            None
        side effects:
            Adds a PSM object to the psms list attribute.
        '''
        self.psms.append(psm)
    
    def _get_xic_windows(self):
        '''
        Calculate the m/z, RT windows to look for XIC peaks in.
        
        arguments:
            None
        returns:
            A list of (m/z low, m/z high, rt start, rt end) tuples representing isotopologue XIC windows.
        side effects:
            None
        '''
        raise NotImplementedError()
    
    def preprocess_ms1s(self, args):
        '''
        Process the collected MS1 peak objects into a data structure that can be used by the transformer model.
        
        arguments:
            args: The parsed options object.
        returns:
            A tuple of (predictor vectors, labels) where labels are optionally None.
        side effects:
            None
        '''
        raise NotImplementedError()
    
    def collect_ms1s(self, rt_ms1_index, mz_ms1_index, args):
        '''
        Collect all MS1 peaks falling within the m/z, RT query windows around the identified PSMs
        
        arguments:
            rt_ms1_index: A SortedList of (RT, MS1 peak) tuples.
            mz_ms1_index: A SortedList of (m/z, MS1 peak) tuples.
            args: The parsed options object.
        returns:
            None
        side effects:
            Populate the ms1s attribute with relavent MS1 peak objects
        '''
        windows = self.get_xic_windows(args)
        for window in windows:
            mz_low, mz_high, rt_start, rt_end = window
            rt_match_set = set(m[1] for m in rt_ms1_index.irange((rt_start,), (rt_end,)))
            mz_match_set = set(m[1] for m in mz_ms1_index.irange((mz_low,), (mz_high,)))
            matched_ms1s = rt_match_set.intersection(mz_match_set)
            self.ms1s.append(list(matched_ms1s))
    
    
    
    




