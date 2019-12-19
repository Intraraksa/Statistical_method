# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:52:30 2019

@author: natdanai.intraraksa
"""

import numpy as np
import math

class norm_dist:
    def __init__(self,var):
        self.var = var
    def mu(self):
        return np.mean(self.var)
    def varian(self):
        return np.var(self.var)
    def std(self):
        return np.std(self.var)
    def prob_normal(self):
        ans = []
        first = 1/(np.sqrt(2*math.pi*self.std()))
        for i in range(self.var.shape[1]):
            second = np.exp(-0.5*((self.var[:,i]-self.mu())/self.mu())**2)
            ans.append(first*second)
        return ans