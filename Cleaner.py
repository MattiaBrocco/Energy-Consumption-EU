import numpy as np
import pandas as pd

class BasicCleaning:
    
    def norm2009(self, df):
        """
        Normalization done on a copy of the input
        """
        self.df = df
        
        df100 = df.copy()
        for c in df100.columns:
            if c != "2009":
                df100[c] = df100[c]/df100["2009"]

        df100["2009"] = 1.0

        return round(df100*100, 1)
    
    
    def car_data(self, data):
        self.data = data
        
        # taking years between 2009, 2016  
        data = data.drop([str(y) for y in np.arange(2000, 2009)] + ["2017"],
                         axis = 1)

        # dropping values we do not need
        data = data.replace(':', np.nan)
        data = data.dropna()
        data = data.drop(data.index[30:], axis = 0)
        data = data.drop(data.index[:2], axis = 0)

        # rename geo\time column
        data = data.rename(columns = {"geo\\time": "GEO"}) 

        # sorted index
        data = data.set_index("GEO")

        # While we were cleaning our df we noticed that in this file did not appear Belgium even if in the others it did
        # Therefore, we add Belgium copypasting values (that are present in the original file!)
        data.loc["Belgium"] = [142.1, 133.4, 127.2, 128, 124, 121.3, 117.9, 115.9]

        # sorting by country 
        data = data.sort_values(by = ["GEO"], axis = 0, ascending = True)

        # convert values to floats since they are strings
        data = data.applymap(lambda s: float(s))
        
        return data
    
    def greenhouse(self, data):
        self.data = data
        
        # Drop rows we will not use
        data = data[data["AIRPOL"] == "Greenhouse gases (CO2, N2O in CO2 equivalent, "+\
                                      "CH4 in CO2 equivalent, HFC in CO2 equivalent, "+\
                                      "PFC in CO2 equivalent, SF6 in CO2 equivalent, NF3 in CO2 equivalent)"]
        data = data[data["AIREMSECT"] == "All sectors (excluding memo items)"].reset_index(drop = True)

        data = data.drop(["UNIT","AIRPOL","AIREMSECT", "Unnamed: 7",
                          "Flag and Footnotes"], axis = 1)

        data["Value"] = data["Value"].astype(float)

        # Pivot data
        data = data[(data["TIME"] >= 2009) &
                    (data["TIME"] <= 2016)].pivot_table(index = "GEO", columns = "TIME",
                                                        values = "Value", aggfunc = np.nansum)

        # rename Germany
        data = data.rename(index = {"Germany (until 1990 former territory of the FRG)": "Germany"})

        data.columns.name = None
        
        data.columns = [str(c) for c in data.columns]
        
        return data
    
    def fertilizers(self, data):
        self.data = data
        
        # changing the values as floats
        data["Value"] = data["Value"].astype(float)

        # drop out-of-scope columns & rows
        data = data.drop(['Flag and Footnotes','UNIT'], axis = 1)

        data = data[~data["GEO"].isin(["European Union - 28 countries",
                                       "European Union (EU6-1958, EU9-1973, EU10-1981, EU12-1986, "+\
                                       "EU15-1995, EU25-2004, EU27-2007, EU28-2013, EU27-2019)"])]

        # create a more-readable pivot table
        data = data[~data["TIME"].isin([2008, 2017])].pivot_table(index = "GEO", columns = "TIME",
                                                                  values = "Value", aggfunc = np.nansum)

        data = data.rename(index = {"Germany (until 1990 former territory of the FRG)":
                                    "Germany"})
        
        data.columns = [str(c) for c in data.columns]
        
        return data
    
    def cattle(self, data):
        self.data = data
        
        # Replace nan
        data = data.replace(":", "0")

        data["Value"] = data["Value"].astype(float)

        # Pivot a specific subset of data
        data = data[(data["ANIMALS"] == "Live bovine animals") &
                    (data["TIME"] >= 2009) &
                    (data["TIME"] <= 2016)].pivot_table(index = "GEO", columns = "TIME",
                                                        values = "Value", aggfunc = np.nansum)

        # INSERTING Italy
        # data took from Istat: 
        # http://agri.istat.it/jsp/dawinci.jsp?q=plB010000010000012000&an=2016&ig=1&ct=201&id=8A%7C9A
        data.loc["Italy"] = [6446.82, 6197.54, 6251.93, 6091.47, 6249.33, 6125.42, 6155.81, 6314.89]

        # Rename Germany
        data = data.rename(index = {"Germany (until 1990 former territory of the FRG)":
                                    "Germany"})
        
        data.columns = [str(c) for c in data.columns]
        
        return data
    
    def renewables(self, data):
        self.data = data
        
        # convert and drop nan
        data = data.replace(":", "0")

        data["Value"] = data["Value"].astype(float)

        # Pivot a specific subset of data
        data = data[(data["UNIT"] == "Thousand tonnes of oil equivalent (TOE)") &
                    (data["PRODUCT"] == "Renewable energies") &
                    (data["TIME"] >= 2009) &
                    (data["TIME"] <= 2016)].pivot_table(index = "GEO", columns = "TIME",
                                                        values = "Value", aggfunc = np.nansum)

        # Rename Germany
        data = data.rename(index = {"Germany (until 1990 former territory of the FRG)":
                                    "Germany"})
        
        data.columns = [str(c) for c in data.columns]
        
        return data