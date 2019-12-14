# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:31:10 2019

@author: natdanai.intraraksa
"""

import numpy as np
import pandas as pd

class basic_static:
    def __init__(self,var):
        self.var = var
#         self.shape = var.shape[0]
    def mean(self):
        return np.mean(self.var)
    def median(self):
        return np.median(self.var)
    def varian(self):
        diff_var = sum((np.array(self.var)-self.mean())**2)
        return diff_var/(np.array(self.var)).shape[0]
    def std_div(self):
        value = np.sqrt(self.varian())
        return value