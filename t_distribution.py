import numpy as np
import random

class t_dist:
    def __init__(self,var,k):
        self.var = var
        self.k = k
    def shuffle(self):
        sample = random.sample(self.var,self.k)
        return sample
    def mu(self):
        return np.mean(self.var)
    def xbar(self):
        return np.mean(self.shuffle())
    def t(self):
        dif_mean = self.xbar()-self.mu()
        return dif_mean/(np.std(self.shuffle())/np.sqrt(len(self.shuffle())))