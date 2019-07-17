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
        print(self.data.POSITION.unique())

    #This method will get the total number of deaths between the two years that that
    #user enters.
    def get_total_deaths_between_years(self, yearOne, yearTwo):
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        number_of_deaths = len(death_data_set)
        return number_of_deaths

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

    #This method will get the data for the third graph
    def get_data_third_graph(self, yearOne, yearTwo):
        religion_death_data = []
        columns = ['Religion', 'Deaths']
        religion_death_data.append(columns)
        religions = ['LUTHERAN CHURCHES', 'METHODIST CHURCHES', 'BAPTIST CHURCHES',
         'PROTESTANT, NO DENOMINATIONAL PREFERENCE', 'SOUTHERN BAPTIST CONVENTION',
         'ROMAN CATHOLIC CHURCH', 'JUDAISM (JEWISH)', 'NO RELIGIOUS PREFERENCE',
         'EPISCOPAL CHURCH', 'ISLAM', 'PRESBYTERIAN CHURCH (USA)',
         'SEVENTH DAY ADVENTIST',
         'CHURCH OF JESUS CHRIST OF LATTER DAY SAINTS (MORMON)', 'BUDDHISM',
         'FRIENDS (QUAKERS)', 'PENTECOSTAL CHURCHES', "JEHOVAH'S WITNESSES"]
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        protestant_deaths = 0
        for religion in religions:
            rows = []
            deaths = int(len(death_data_set[(death_data_set.RELIGION == religion)]))
            #I want to collectivelly count all of these religions as protestant thus
            #I create a count that will track number of deaths for the religion.
            if religion == 'LUTHERAN CHURCHES' or religion == 'METHODIST CHURCHES' or \
            religion == 'BAPTIST CHURCHES' or religion == 'PROTESTANT, NO DENOMINATIONAL PREFERENCE' or \
            religion == 'SOUTHERN BAPTIST CONVENTION' or religion == 'EPISCOPAL CHURCH' or \
            religion == 'PRESBYTERIAN CHURCH (USA)' or religion == 'SEVENTH DAY ADVENTIST' or \
            religion == 'FRIENDS (QUAKERS)' or religion == 'PENTECOSTAL CHURCHES':
                protestant_deaths = deaths + protestant_deaths
            if religion == "JEHOVAH'S WITNESSES":
                protestant_deaths = deaths + protestant_deaths
                rows.append('PROTESTANT')
                rows.append(protestant_deaths)
                religion_death_data.append(rows)
            elif religion == 'ROMAN CATHOLIC CHURCH' or religion == 'JUDAISM (JEWISH)' or \
            religion == 'NO RELIGIOUS PREFERENCE' or religion == 'ISLAM' or \
            religion == 'CHURCH OF JESUS CHRIST OF LATTER DAY SAINTS (MORMON)':
                rows.append(religion)
                rows.append(deaths)
                religion_death_data.append(rows)
        return religion_death_data

    #This method will get the data for the fourth graph
    def get_data_fourth_graph(self, yearOne, yearTwo):
        race_death_data = []
        columns = ['Race', 'Deaths']
        race_death_data.append(columns)
        races = ['WHITE', 'BLACK OR AFRICAN AMERICAN']
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        for race in races:
            rows = []
            deaths = int(len(death_data_set[(death_data_set.ETHNICITY == race)]))
            rows.append(race)
            rows.append(deaths)
            race_death_data.append(rows)
        return race_death_data

    #This method will get the data for the fifth graph which deals with enlisted
    #ranks
    def get_data_fifth_graph(self, yearOne, yearTwo):
        enlisted_death_data = []
        columns = ['Rank', 'Deaths']
        enlisted_death_data.append(columns)
        ranks = ['PVT', 'PFC', 'LCPL', 'CPL', 'SP4', 'SGT', 'SSGT', 'SSG', 'SFC',
        'GYSGT', 'MSGT', 'MSG', '1STSGT', '1SG', 'MGYSGT', 'SGTMAJ']
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        E4_deaths = 0
        E6_deaths = 0
        E7_deaths = 0
        E8_deaths = 0
        E9_deaths = 0
        for rank in ranks:
            rows = []
            deaths = int(len(death_data_set[(death_data_set.RANK == rank)]))
            if rank == 'CPL' or rank == 'SP4':
                E4_deaths = deaths + E4_deaths
                if rank == 'SP4':
                    rows.append('Cpl')
                    rows.append(E4_deaths)
                    enlisted_death_data.append(rows)
            elif rank == 'SSGT' or rank == 'SSG':
                E6_deaths = deaths + E6_deaths
                if rank == 'SSG':
                    rows.append('SSgt')
                    rows.append(E6_deaths)
                    enlisted_death_data.append(rows)
            elif rank == 'SFC' or rank == 'GYSGT':
                E7_deaths = deaths + E7_deaths
                if rank == 'GYSGT':
                    rows.append('GYSgt')
                    rows.append(E7_deaths)
                    enlisted_death_data.append(rows)
            elif rank == 'MSGT' or rank == 'MSG' or rank == '1STSGT' or rank == '1SG':
                E8_deaths = deaths + E8_deaths
                if rank == '1SG':
                    rows.append('1st Sgt')
                    rows.append(E7_deaths)
                    enlisted_death_data.append(rows)
            elif rank == 'MGYSGT' or rank == 'SGTMAJ':
                E9_deaths = deaths + E9_deaths
                if rank == 'SGTMAJ':
                    rows.append('SGTMAJ')
                    rows.append(E9_deaths)
                    enlisted_death_data.append(rows)
            else:
                rows.append(rank)
                rows.append(deaths)
                enlisted_death_data.append(rows)
        return enlisted_death_data

    #This method will get the data for the sixth graph which deals with officer
    #ranks
    def get_data_sixth_graph(self, yearOne, yearTwo):
        officer_death_data = []
        columns = ['Rank', 'Deaths']
        officer_death_data.append(columns)
        ranks = ['2LT', '2NDLT', '1LT', '1STLT', 'CPT','CAPT', 'MAJ', 'LTC',
        'LTCOL', 'COL']
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        secondLt_deaths = 0
        firstLt_deaths = 0
        capt_deaths = 0
        LTC_deaths = 0
        for rank in ranks:
            rows = []
            deaths = int(len(death_data_set[(death_data_set.RANK == rank)]))
            if rank == '2LT' or rank == '2NDLT':
                secondLt_deaths = deaths + secondLt_deaths
                if rank == '2NDLT':
                    rows.append('2nd Lt')
                    rows.append(secondLt_deaths)
                    officer_death_data.append(rows)
            elif rank == '1LT' or rank == '1STLT':
                firstLt_deaths = deaths + firstLt_deaths
                if rank == '1STLT':
                    rows.append('1st Lt')
                    rows.append(firstLt_deaths)
                    officer_death_data.append(rows)
            elif rank == 'CPT' or rank == 'CAPT':
                capt_deaths = deaths + capt_deaths
                if rank == 'CAPT':
                    rows.append('Capt')
                    rows.append(capt_deaths)
                    officer_death_data.append(rows)
            elif rank == 'LTC' or rank == 'LTCOL':
                LTC_deaths = deaths + LTC_deaths
                if rank == 'LTCOL':
                    rows.append('Lt Col')
                    rows.append(LTC_deaths)
                    officer_death_data.append(rows)
            else:
                rows.append(rank)
                rows.append(deaths)
                officer_death_data.append(rows)
        return officer_death_data

    #This method will get the data for the seventh graph which deals with warrant officer
    #ranks
    def get_data_seventh_graph(self, yearOne, yearTwo):
        warrant_officer_death_data = []
        columns = ['Rank', 'Deaths']
        warrant_officer_death_data.append(columns)
        ranks = ['WO-1', 'WO1', 'CW2', 'CWO2', 'CW3', 'CWO3', 'CWO-4', 'CW4', 'CWO4']
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        WO1_deaths = 0
        W02_deaths = 0
        WO3_deaths = 0
        W04_deaths = 0
        for rank in ranks:
            rows = []
            deaths = int(len(death_data_set[(death_data_set.RANK == rank)]))
            if rank == 'WO-1' or rank == 'WO1':
                WO1_deaths = deaths + WO1_deaths
                if rank == 'WO1':
                    rows.append('WO-1')
                    rows.append(WO1_deaths)
                    warrant_officer_death_data.append(rows)
            elif rank == 'CW2' or rank == 'CWO2':
                W02_deaths = deaths + W02_deaths
                if rank == 'CWO2':
                    rows.append('CWO-2')
                    rows.append(W02_deaths)
                    warrant_officer_death_data.append(rows)
            elif rank == 'CW3' or rank == 'CWO3':
                WO3_deaths = deaths + WO3_deaths
                if rank == 'CWO3':
                    rows.append('CWO-3')
                    rows.append(WO3_deaths)
                    warrant_officer_death_data.append(rows)
            elif rank == 'CWO-4' or rank == 'CW4' or rank == 'CWO4':
                W04_deaths = deaths + W04_deaths
                if rank == 'CWO4':
                    rows.append('CWO-4')
                    rows.append(W04_deaths)
                    warrant_officer_death_data.append(rows)
            else:
                rows.append(rank)
                rows.append(deaths)
                warrant_officer_death_data.append(rows)
        return warrant_officer_death_data

    #This method will get the data for the eigth chart which will focus on deaths
    #by MOS
    def get_data_eight_graph(self, yearOne, yearTwo):
        MOS_death_data = []
        columns = ['MOS', 'Deaths']
        MOS_death_data.append(columns)
        jobs = ['INFANTRYMAN', 'RIFLEMAN', 'FIELD ARTILLERY BASIC', 'MACHINEGUNNER'
         'ASSAULTMAN', 'ARMOR CREWMAN', 'MORTARMAN', 'RADIOMAN', 'COMBAT PHOTOGRAPHER/MOTION MEDIA',
         'LAV ASSAULTMAN', 'BASIC TANK AND ASSAULT AMPHIBIOUS VEHICLE CREWMAN',
         'SPECIAL FORCES']
        death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]
        for job in jobs:
            rows = []
            deaths = int(len(death_data_set[(death_data_set.POSITION == job)]))
            rows.append(job)
            rows.append(deaths)
            MOS_death_data.append(rows)
        return MOS_death_data



# one = Data()
# one.basic_info()
# one.get_data_eight_graph(1960, 1965)
