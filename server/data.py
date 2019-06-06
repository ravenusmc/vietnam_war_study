#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/VietnamConflict.csv')

    def basic_info(self):
        print(self.data.head())
        
one = Data()
one.basic_info()
