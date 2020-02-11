import pandas as pd
import numpy as np
import os
import json
import random as rnd
# Changing directory to proper directory
os.chdir('CITY')
# reading json data
files = []
for file in os.listdir():
    if file.endswith('.json'):
        files.append(file)
df = pd.read_json(files[0])
# Extracitng cord elem
dic = {}
dics = df['coord']
lat = []
lon = []
# Loop to get dictionaries by dictionary to get lattitude and longtitude
for dic in dics:
    lat.append(dic.get('lat'))
    lon.append(dic.get('lon'))
lat = np.array(lat)
lon = np.array(lon)
df["lat"]=lat
df["lon"] = lon

'''
Class City to get information about City which are interesing for me 
id 
name 
lattitude 
longtitude
county
Five parameters about city to get proper map of cities

'''
class City_Data():

    def __init__(self,city):
        self.city = city
        self.id = df[df["name"]==city]["id"].values[0]
        self.country = df[df["name"]==city]["country"].values[0]
        self.lat = df[df["name"]==city]["lat"].values[0]
        self.lon = df[df["name"]==city]["lon"].values[0]
    def __str__(self):
       return "City {} has a coordinates {} {} and it belongs to {}".format(self.city,self.lat,self.lon,self.country)
# Random number
 '''
Get cities id using random seeds generator
Parameter: number_of_cities - how many ids you want to get
'''
def cities_id(number_of_cities):
    array_id = df.loc[:,"id"].values
    return np.random.choice(array_id,number_of_cities)




if __name__ == "__main__":
    'City is here'
    print(np.random.choice(df.loc[:,"id"].values,20))
