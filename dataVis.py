import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import geopandas as gpd

data = pd.read_csv('data.csv')
data['chargper'] = np.where(data['nbrtotc']>0,data.chargtot / data.nbrtotc,0)
shp = gpd.read_file(r'./shape_file/npc96_region_Project1.shp')
shp = shp.sort_values(by='POSTCODE')

perPostal = data.groupby(['CODPOSS'])['duree'].sum().reset_index()
perPostal = perPostal.rename(columns={'CODPOSS':'POSTCODE'})
shp = pd.merge(shp,perPostal,how='left',on='POSTCODE')
shp.duree = shp.duree.fillna(0)

shp.plot(column='duree', legend=True,cmap='jet')



fig, axes = plt.subplots(nrows=2, ncols=3)
plt.figure(2)
# info policy holders
data.groupby(['AGEPH'])['duree'].sum().plot(kind='line',xlabel='Age',ylabel='Total exposure',ax=axes[0,0])
data.groupby(['nbrtotc'])['duree'].sum().plot(kind='bar',xlabel='Number of claims',ylabel='Total exposure',ax=axes[0,1])
data.groupby(['sexp'])['duree'].sum().plot(kind='bar',xlabel='Sex',ylabel='Total exposure',ax=axes[0,2])
data.groupby(['split'])['duree'].sum().plot(kind='bar',xlabel='Split of premium',ylabel='Total exposure',ax=axes[1,0])
data.groupby(['coverp'])['duree'].sum().plot(kind='bar',xlabel='Type of coverage',ylabel='Total exposure',ax=axes[1,1])
data.groupby(['chargtot'])['duree'].sum().plot(kind='line',xlabel='Charge for total claims',ylabel='Total exposure',ax=axes[1,2])

fig, axes = plt.subplots(nrows=2, ncols=3)
plt.figure(3)
# info cars
data.groupby(['agecar'])['duree'].sum().plot(kind='bar',xlabel='Age of car',ylabel='Total exposure',ax=axes[0,0])
data.groupby(['usec'])['duree'].sum().plot(kind='bar',xlabel='Type of use',ylabel='Total exposure',ax=axes[0,1])
data.groupby(['fuelc'])['duree'].sum().plot(kind='bar',xlabel='Type of fuel',ylabel='Total exposure',ax=axes[0,2])
data.groupby(['fleetc'])['duree'].sum().plot(kind='bar',xlabel='Fleet or not',ylabel='Total exposure',ax=axes[1,0])
data.groupby(['sportc'])['duree'].sum().plot(kind='bar',xlabel='Sports car or not',ylabel='Total exposure',ax=axes[1,1])
data.groupby(['powerc'])['duree'].sum().plot(kind='bar',xlabel='Power of car',ylabel='Total exposure',ax=axes[1,2])

plt.show()