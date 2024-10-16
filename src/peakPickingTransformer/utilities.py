#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:19:07 2024

@author: anon
"""

def load_training_data(args):
    '''
    Load the training data from Henning et al. and process it into data structures suitable for training.
    
    arguments:
        args: The parsed options object.
    returns:
        A list of labeled feature objects.
    side effects:
        None
    
    Implementation notes: Andrew this function is going to be my problem because I will have to do the
    training data setup in a script outside of this tool.
    '''
    raise NotImplementedError()

def split_data(features, args):
    '''
    Split labeled data into train and test subsets.
    
    arguments:
        features: A list of labeled feature objects.
        args: The parsed options object.
    returns:
        A tuple of (train_features, test_features) wich are random, disjoint subsets of the provided data.
    side effects:
        None
    '''
    import numpy as np
    rng = np.random.default_rng(args.seed)
    
    train_idxs = rng.choice(range(len(features)), args.split_frac, replace = False)
    test_idxs = list(set(range(len(features))).difference(train_idxs))
    return (features[train_idxs], features[test_idxs])
    

def assess_model(features, model, args):
    '''
    Run inference on the test dataset and generate quality control plots.
    
    arguments:
        features: A list of labeled feature objects.
        model: The trained transformer model.
        args: The parsed options object.
    returns:
        None
    side effects:
        Save a series of quality control plots.
    
    Implementation notes: We should save traces of model performance during training with the model object and then plot those here
    in addition to whatever we want to plot from the test set results.
    '''
    raise NotImplementedError()

def get_ms1s(args):
    '''
    Parses mzML file and generates indexed data structures for fast lookup.
    
    arguments:
        args: The parsed options object.
    returns:
        A tuple of (MS1 objects sorted by m/z, MS1 objects sorted by RT)
    side effects:
        None
    '''
    from sortedcontainers import SortedList
    import pymzml
    
    mzml = pymzml.run.Reader(args.mzml_file)
    ms1s = []
    




