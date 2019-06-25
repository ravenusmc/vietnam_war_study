#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/VietnamConflict.csv')

    #This is just a test method that's used for for testing ideas out.
    def basic_info(self):
        print(self.data.head())

    #This method will get the total number of deaths between the two years that that
    #user enters.
    def get_total_deaths_between_years(self, yearOne, yearTwo):
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        number_of_deaths = len(death_data_set)
        return number_of_deaths

    #This method will get the total number of deaths by year
    def get_number_of_death(self):
        pass

one = Data()
one.basic_info()
