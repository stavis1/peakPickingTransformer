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
        An X, Y tuple of training features and labels, respectively.
    side effects:
        None
    
    Implementation notes: Andrew this function is going to be my problem because I will have to do the
    training data setup in a script outside of this tool.
    '''
    raise NotImplementedError()

def split_data(X, Y, args):
    '''
    Split labeled data into train and test subsets.
    
    arguments:
        X: A collection of predictors.
        Y: A collection of labels.
        args: The parsed options object.
    returns:
        A tuple of X_train, Y_train, X_test, Y_test wich are random, disjoint subsets of the provided data.
    side effects:
        None
    '''
    raise NotImplementedError()

