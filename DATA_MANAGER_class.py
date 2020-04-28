import pandas as pd
import numpy as np

class data_manager:
    df = None
    
    def floats_1(self, df): # to change values entering from "Value" column
        self.df = df
        L = []
        for n in range(len(df["Value"])):
            L += [float(df["Value"][n].replace(",",""))]
            df.loc[n:n,"Value"] = L[n]
    
    def floats_2(self, df): # to change values entering from the years of the df. For those that do not have "Value"
        
        """
          The floats_2 function is for those datasets that originally did not have the column "Value",
          so it changes data into floats from "Years"
        """
        
        self.df = df
        R = []
        for y in range(2009,2017):
            if str(y) in df:
                for n in range(len(df[str(y)])):
                    R += [float(df[str(y)][n])]
                    df[str(y)][n] = R[n] 
                R = []
                
    def one_decimal(self, df): 
        self.df = df
        for i in range(len(df.values)):
            if type(df.values[i]) != int:
                df.values[i] = np.round(df.values[i],1)
            
    def norm(self, df):
        
        """
          This function is to create percentage-normalized datasets in a 100-base with respect to 2009 as 100%
        """
        
        self.df = df
        common_states_and_EU = ['Austria', 'Belgium', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'Poland', 'Portugal', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom', 'EU (23 Countries)']
        for y in range(2016,2008,-1):
            if y in df:
                for c in common_states_and_EU:
                    df.loc[c, y] = (df.loc[c,y]/df.loc[c,2009])*100
