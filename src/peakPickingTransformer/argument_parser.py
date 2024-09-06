#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:31:47 2024

@author: 4vt
"""

import argparse
import os

class ArgumentError(Exception):
    '''
    This exception is raised when invalid command line arguments are provided.
    '''
    pass

class Args():
    '''
    This class parses, validates and stores command line arguments    
    '''
    def __init__(self):
        '''
        Parses command line arguments.
        
        arguments:
            None
        returns:
            an object of class Args
        side effects:
            None
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('--psms', 
                            required = False,
                            default = False, 
                            action = 'store',
                            help = 'The TSV file of PSMs to quantify.')
        parser.add_argument('--mzml', 
                            required = False,
                            default = False, 
                            action = 'store',
                            help = 'The mzML file to quantify.')
        parser.add_argument('--model', 
                            required = False,
                            default = False, 
                            action = 'store',
                            help = 'The fitted model weights.')
        parser.add_argument('--output', 
                            required = False,
                            default = False, 
                            action = 'store',
                            help = 'The prefix for all output files.')
        parser.add_argument('--task', 
                            required = True, 
                            action = 'store',
                            choices = ['train', 'refine', 'infer'],
                            help = 'whether to train a model, refine an existing model, or run inference using a trained model.')
        #args now holds each of the command line parameters as an attribute
        #whose value is passed from the command line.
        args = parser.parse_args()
        
        #__dict__ is an attribute of (nearly) all python objects that stores all methods and attributes 
        #of that object. What we're doing here is grabbing all attributes from args that don't start
        #with _ meaning that they are command line parameters and adding them to this instantiation of
        #our custom Args() class.
        self.__dict__.update((i for i in args.__dict__.items() if not i[0].startswith('_')))

    def validate_args(self):
        '''
        raises an error if the command line arguments are invalid
        
        arguments:
            None
        returns:
            None
        side effects:
            None
        raises:
            ArgumentError on invalid command line arguments
        '''
        
        #make sure that all of the arguments required for a task are provided
        if self.task == 'train':
            required = [self.output]
        if self.task == 'refine':
            required = [self.output, self.psms, self.mzml, self.model]
        if self.task == 'infer':
            required = [self.output, self.psms, self.mzml, self.model]
        
        for req in required:
            if not req:
                raise ArgumentError('You are missing required command line arguments.')
        
        #make sure all of the provided files exist
        for file in [self.psms, self.mzml, self.model]:
            if not os.path.exists(file):
                raise ArgumentError('One or more of the provided files does not exist.')
        