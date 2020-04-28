import pandas as pd
import numpy as np

class geo:
    df = None
    
    def common_states(self, df): # to obtain in each dataframe the same Countries
        
        """
          This function is to obtain the same countries in each dataframe (with the drop built-in function)
          starting from the common_states list composed as shown in the .ipynb file
        """
        
        self.df = df
        common_states = ['Austria', 'Belgium', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'Poland', 'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']
        for c in df.index :
            if c not in common_states:
                df.drop(df[df.index== c].index, inplace=True)
        
        
    def add_EU(self, df):
        
        """
          To add at the bottom of the dataframe the sum of all the values
          to show the total in each year in the Area we are analyzing
        """
        
        self.df = df
        df.loc["EU (23 Countries)"] = df.sum()
    
    
    def EU_mean(self, df): # to add at the bottom of the table the mean of all the values for each year
        self.df = df
        df.loc["EU (23 Countries)"] = df.mean()
        
        
    def table_for_country(self, country_code, df, country):
        
        """
          To obtain a cumulative table for each country and summarize data
          with this order
        """
        
        self.df = df
        country_code = df.copy()
        country_code.drop(country_code[country_code.GEO != country].index, inplace=True)
        country_code = country_code.rename(columns = {"Dataframe": country})
        country_code.set_index(country, inplace = True)
        country_code.drop("GEO", axis = 1, inplace = True)
        return country_code