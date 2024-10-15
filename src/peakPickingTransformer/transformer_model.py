#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:05:23 2024

@author: compbiolover
"""

class transformer():
    '''This class holds the transformer model.'''
    def _transformer_model(self):
        '''
        Define the transformer model.
        
        arguments:
            None
        returns:
            A compiled torch model object.
        side effects:
            None
        '''
        raise NotImplementedError()
    
    def fit(self, X, Y, args):
        '''
        Fit the model to training data and returns a fitted model object.
        
        arguments:
            X: An array of preprocessed predictor tensors.
            Y: An array of label vectors.
            args: The parsed options object.
        returns:
            A reference to the instantiated object.
        side effects:
            Adds a self.model property that contains the fitted model.
        '''
        self.model = self._transformer_model()
        #fit model
        raise NotImplementedError()
        return self
    
    def refine(self, X, Y, args):
        '''
        Update the weights of a pretrained model with new training data and returns a fitted model object.
        
        arguments:
            X: An array of preprocessed predictor tensors.
            Y: An array of label vectors.
            args: The parsed options object.
        returns:
            A reference to the instantiated object.
        side effects:
            Updates the weights of self.model.
        '''
        #fit self.model
        raise NotImplementedError()
        return self
    
    def load(self, args):
        '''
        Load a fitted model from a file and returns a fitted model object.
        
        Arguments:
            args: The parsed options object.
        returns:
            A reference to the instantiated object.
        side effects:
            Adds a self.model property that contains the fitted model.
        
        Implementation notes: The location of the fitted weights will be in the args object.
        '''
        self.model = self._transformer_model()
        #load model weights
        raise NotImplementedError()
        return self
    
    def dump(self, args):
        '''
        Save a fitted model to a file.
        
        Arguments:
            args: The parsed options object.
        returns:
            None
        side effects:
            The model weights are saved to a file.
        
        Implementation notes: The location of the fitted weights will be in the args object.
        '''
        raise NotImplementedError()
    
    def _make_XIC_peaks(self, Ŷ, args):
        '''
        Find XIC peaks from the per-MS1-peak predicted probabilites given by the model.
        
        arguments:
            Ŷ: The array of predicted probabilies for each MS1 peak belonging to an XIC peak e.g. Pr(Y = 1) for each element of X.
            args: The parsed options object.
        returns:
            A list of XIC peak objects, the list may be empty.
        side effects:
            None
        
        Implementation notes: There will likely need to be some kind of heuristic filtering done in this step.
        For example XIC peaks should have a minimum length and maximum Δm/z. 
        This would be the logical place to put that kind of filtering.
        '''
        raise NotImplementedError()
    
    def predict(self, feature, args):
        '''
        Predict features from a collection of preprocessed predictor vectors.
        
        arguments:
            feature: A feature object containing preprocessed MS1 peak objects.
            args: The parsed options object.
        returns:
            The feature object with the XIC obect list populated
        side effects:
            None        
        '''
        #predict the raw Ŷ values using the fitted transformer model
        #post-process these into a collection of XIC peak objects
        #add the XIC objects to the feature object
        raise NotImplementedError()
    