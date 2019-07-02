#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/VietnamConflict.csv')

    #This is just a test method that's used for for testing ideas out. This method
    #is only meant to help me test out ideas and not to 'test' the application
    def basic_info(self):
        print(self.data.head())
        #This will get me all unique values in a column
        print(death_data_set.BRANCH.unique())

    #This method will get the total number of deaths between the two years that that
    #user enters.
    def get_total_deaths_between_years(self, yearOne, yearTwo):
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        number_of_deaths = len(death_data_set)
        return number_of_deaths

    #This method will get the total number of deaths by year.
    # def get_number_of_deaths_total(self):
    #     #Getting the minimum year
    #     first_year = self.data['FATALITY_YEAR'].min()
    #     #Setting the max year. I noticed that the data goes up to 2006 but wanted
    #     #to focus on the war.
    #     last_year = 1975
    #     death_data = []
    #     #setting up a while loop to get number of deaths per year.
    #     while first_year <= last_year:
    #         year_data = {}
    #         deaths_by_year = self.data[(self.data.FATALITY_YEAR == first_year)]
    #         year_data['Year'] = int(first_year)
    #         year_data['Deaths'] = int(len(deaths_by_year))
    #         first_year += 1
    #         death_data.append(year_data)
    #     return death_data

    #This method will get the total number of deaths by year. This formatted the
    #data the way that Google charts wanted it.
    def get_number_of_deaths_total(self):
        #Getting the minimum year
        first_year = self.data['FATALITY_YEAR'].min()
        #Setting the max year. I noticed that the data goes up to 2006 but wanted
        #to focus on the war.
        last_year = 1975
        death_data = []
        columns = ['Year', 'Deaths']
        death_data.append(columns)
        #setting up a while loop to get number of deaths per year.
        while first_year <= last_year:
            rows = []
            deaths_by_year = self.data[(self.data.FATALITY_YEAR == first_year)]
            #death_data[first_year] = int(len(deaths_by_year))
            rows.append(int(first_year))
            rows.append(int(len(deaths_by_year)))
            death_data.append(rows)
            first_year += 1
        # print(death_data)
        return death_data

    #This method will get the data for the second graph.
    def get_data_second_graph(self, yearOne, yearTwo):
        branch_death_data = []
        columns = ['Branch', 'Deaths']
        branch_death_data.append(columns)
        branches = ['ARMY', 'AIR FORCE', 'MARINE CORPS', 'NAVY', 'COAST GUARD']
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        for branch in branches:
            rows = []
            #This will get the number of deaths for each branch of service in between
            #the two years that a user enters.
            deaths = int(len(death_data_set[(death_data_set.BRANCH == branch)]))
            rows.append(branch)
            rows.append(deaths)
            branch_death_data.append(rows)
        return branch_death_data



one = Data()
one.get_data_second_graph(1960, 1975)
