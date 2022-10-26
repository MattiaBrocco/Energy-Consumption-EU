import os
import json
import folium
from pylab import *
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Visualizations:
    """
      Cartesian function is to create five subplots (lineplots)
      for each Country and then to save these graph in a .jpg file
    """
    def cartesian(self, class_call, country_code, country, bigdata):
        
        self.country = country
        self.bigdata = bigdata
        self.class_call = class_call
        self.country_code = country_code
        
        eu_data = bigdata[bigdata["GEO"] == "EU (26 Countries)"].set_index("Dataframe").drop("GEO", axis = 1)
        data_plot = bigdata[bigdata["GEO"] == country].set_index("Dataframe").drop("GEO", axis = 1)
        
        
        plt.figure(figsize = (10, 13), tight_layout = True)
        
        subplot(3, 2, 1)
        plt.plot(eu_data.columns.values,
                 eu_data.loc["Average CO2 emissions per km from new passenger cars"].tolist(),
                 ".b-", label= "EU", linewidth = 0.8)
        plt.plot(data_plot.columns.values,
                 data_plot.loc["Average CO2 emissions per km from new passenger cars"].tolist(),
                 "or-", label = str(country), linewidth = 1)
        plt.xlabel("Year", fontsize = 9)
        plt.ylabel("Percentage ", fontsize = 9)
        plt.title("Average CO2 emissions per km from new passenger cars", fontsize = 11)
        plt.legend(loc = "upper left", fontsize = 10)
        plt.ylim(65,110)
        
        
        subplot(3, 2, 2)
        plt.plot(eu_data.columns.values,
                 eu_data.loc["Greenhouse emissions by source sector"].tolist(),
                 ".b-", label = "EU", linewidth = 0.8)
        plt.plot(data_plot.columns.values,
                 data_plot.loc["Greenhouse emissions by source sector"].tolist(), "or-",
                 label = str(country), linewidth = 1)
        plt.xlabel("Year", fontsize = 9)
        plt.ylabel("Percentage ", fontsize = 9)
        plt.title("Greenhouse emissions by source sector", fontsize=11)
        plt.legend(loc = "upper left", fontsize = 10)
        plt.ylim(45,165)
        
        subplot(3,2,3)
        plt.plot(eu_data.columns.values,
                 eu_data.loc["Consumption of inorganic fertilizers"].tolist(),
                 ".b-", label = "EU", linewidth = 0.8)
        plt.plot(data_plot.columns.values,
                 data_plot.loc["Consumption of inorganic fertilizers"].tolist(),
                 "or-", label = str(country), linewidth = 1)        
        plt.xlabel("Year", fontsize = 9)
        plt.ylabel("Percentage ", fontsize = 9)
        plt.title("Consumption of inorganic fertilizers", fontsize = 11)
        plt.legend(loc = "upper left", fontsize = 10)
        plt.ylim(85, 165)
        
        subplot(3,2,4)
        plt.plot(eu_data.columns.values,
                 eu_data.loc["Bovine population"].tolist(),
                 ".b-", label = "EU", linewidth = 0.8)
        plt.plot(data_plot.columns.values,
                 data_plot.loc["Bovine population"].tolist(),
                 "or-", label = str(country), linewidth = 1)        
        plt.xlabel("Year", fontsize = 9)
        plt.ylabel("Percentage ", fontsize = 9)
        plt.title("Bovine population", fontsize = 11)
        plt.legend(loc = "upper left", fontsize = 10)
        plt.ylim(80,125)
        
        subplot(3,2,5)
        plt.plot(eu_data.columns.values,
                 eu_data.loc["Supply, transformation and consumption of renewable energies"].tolist(),
                 ".b-", label = "EU", linewidth = 0.8)
        plt.plot(data_plot.columns.values,
                 data_plot.loc["Supply, transformation and consumption of renewable energies"].tolist(),
                 "or-", label = str(country), linewidth = 1)        
        plt.xlabel("Year", fontsize = 9)
        plt.ylabel("Percentage ", fontsize = 9)
        plt.title("Supply, transformation and consumption of renewable energies", fontsize = 11)
        plt.legend(loc = "upper left", fontsize = 10)
        plt.ylim(85,240)
        
        if "country_figs" not in os.listdir():
            os.mkdir(os.getcwd() + "\\country_figs")
        
        plt.savefig("{}\\country_figs\\{}.jpg".format(os.getcwd(),
                                                      country), dpi = 300)
        
     
    def icon_map(self, image, df, divided_by):
        """
        This function is to create the icon map
        (where paramteres are the .png file to be chosen, the dataframe and the number
        to divide the size to due to the difference in terms of magnitude of values
        between the datasets) starting from a dictionarywith the proper decimal
        coordinates where each marker is going to be located
        """
        coord = {"Austria": [47.458835, 14.556134], "Belgium": [50.789134, 4.384886],
                 "Czechia": [49.897642, 14.505872], "Denmark": [55.537183, 12.684984],
                 "Estonia": [59.408057, 24.818697], "Finland": [61.129879, 24.936323],
                 "France": [47.666409, 2.220547], "Germany": [51.770197, 10.199126],
                 "Greece": [38.05109, 23.853072], "Hungary": [46.941787, 18.956347],
                 "Ireland": [53.251135, -6.155177], "Italy": [41.9109, 12.4818],
                 "Latvia": [56.872143, 24.197988], "Lithuania": [54.596624, 25.32752],
                 "Luxembourg": [49.616817, 6.131143], "Netherlands": [52.334385, 4.897413],
                 "Poland": [52.224573, 20.968351], "Portugal": [38.668402, -9.154653],
                 "Slovakia": [48.76347, 19.601031], "Slovenia": [46.061838, 14.507237],
                 "Spain": [40.375889, -3.665597], "Sweden": [59.263103, 18.118232],
                 "United Kingdom": [51.340944, -0.10122]}

        
        mapp = folium.Map(location=[54.5260, 15.2551],
                          tiles = "OpenStreetMap", zoom_start = 4)

        for k,v in coord.items():
            folium.Marker(v, tooltip = k,
                      icon = folium.features.CustomIcon(image,
                      icon_size = (((df.loc[k, "2009"] + df.loc[k, "2010"] +\
                                     df.loc[k, "2011"] + df.loc[k, "2012"] +
                                     df.loc[k, "2013"] + df.loc[k, "2014"] +\
                                     df.loc[k, "2015"] + df.loc[k, "2016"]) / divided_by),
                                   ((df.loc[k, "2009"] + df.loc[k, "2010"] +\
                                     df.loc[k, "2011"] + df.loc[k, "2012"] +
                                     df.loc[k, "2013"] + df.loc[k, "2014"] +\
                                     df.loc[k, "2015"] + df.loc[k, "2016"]) / divided_by)))).add_to(mapp) 
        return mapp

    
    def choropleth(self, df, title_of_map, second_parameter, color):
        """
          To create the choropleth, where first a map is initialized, then thanks to a .json file
          that gives the borders of each state we set a palette of color for the shown shades
        """
        self.df = df
        self.color = color
        self.title_of_map = title_of_map
        self.second_parameter = second_parameter
        
        m = folium.Map(location=[54.160231234635866, 13.540297474999988],
                       tiles = "OpenStreetMap", zoom_start = 3.5)
        
        # WORK ON IT !!!
        # json_reference = json.load(open("eu-countries.geo.json"))
        # json_countries = [json_reference["features"][i]["properties"]["sovereignt"]
        #                   for i in range(len(json_reference["features"]))]
        
        # data_to_plot = df[df.index.isin(json_countries)].reset_index(drop = True).copy()
        
        m.choropleth(geo_data = "eu-countries.geo.json", name = title_of_map,
                     data = df,
                     columns = [df.index, second_parameter],
                     key_on = "feature.properties.sovereignt",
                     fill_color = color, fill_opacity = 0.9,
                     line_opacity = 0.5)
        
        folium.LayerControl().add_to(m)
        
        return m
