"""
Visualisation of input data
- visualisation of exposure per area using shapefile
- visualisation of exposure per parameter concerning info on policyholder
- visualisation of exposure per parameter concerning info on car
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import geopandas as gpd

# DATA INPUT
data = pd.read_csv('data.csv')
data['nbrtotp'] = data.nbrtotc/data.duree
shp = gpd.read_file(r'./shape_file/npc96_region_Project1.shp')
shp = shp.sort_values(by='POSTCODE')

perPostal = data.groupby(['CODPOSS'])['duree'].sum().reset_index()
perPostal['mean_nbrtotp'] = data.groupby(['CODPOSS'])['nbrtotp'].mean().reset_index().nbrtotp
perPostal = perPostal.rename(columns={'CODPOSS':'POSTCODE'})
shp = pd.merge(shp,perPostal,how='left',on='POSTCODE')
shp.duree = shp.duree.fillna(0)
shp.mean_nbrtotp = shp.mean_nbrtotp.fillna(0)




# data.boxplot(column='nbrtotc',by='split')

# RESPONSE VARIABLES
fig, axes = plt.subplots(nrows=1, ncols=3)
plt.figure(1)
data.nbrtotc.value_counts(normalize=True).plot(kind='bar',xlabel='Exposure',ylabel='Relative exposure',ax=axes[0])
data.duree.plot(kind='hist',xlabel='Exposure',ylabel='Relative exposure',ax=axes[0])
data.nbrtotc.value_counts(normalize=True).plot(kind='bar',xlabel='Number of claims',ylabel='Relative exposure',ax=axes[1])
data.nbrtotc.plot(kind='hist',xlabel='Number of claims',ylabel='Relative exposure',ax=axes[1])
#data.chargtot.plot(kind='density',logx=True,xlabel='Total claim amount',ylabel='Relative exposure',ax=axes[2])
data['nbrotc'>0].chargtot.plot(kind='hist',xlim=(0,1e5),xlabel='Age',ylabel='Total exposure',bins=300,weights=np.ones(len(data['nbrotc'>0])) / len(data['nbrotc'>0]),ax=axes[2])

fig.suptitle('Response variables')
# some statistics on response variables
exposure_summary = data.duree.value_counts(normalize=True)
claim_summary = data.nbrtotc.value_counts(normalize=True)
claim_frequency = data.nbrtotc.sum()/data.duree.sum()
# number of claims higher than 10k if there was a claim
large_claim = data[data.chargtot>10000].shape[0]/data[data.chargtot>0].shape[0]
claim_severity = data.chargtot.sum()/data.nbrtotc.sum()

fig, axes = plt.subplots(nrows=2, ncols=5)
plt.figure(2)
# info policy holders
data.coverp.value_counts(normalize=True).plot(kind='bar',xlabel='Type of coverage',ylabel='Total exposure',ax=axes[0,0])
data.fuelc.value_counts(normalize=True).plot(kind='bar',xlabel='Type of fuel',ylabel='Total exposure',ax=axes[0,1])
data.sexp.value_counts(normalize=True).plot(kind='bar',xlabel='Sex',ylabel='Total exposure',ax=axes[0,2])
data.usec.value_counts(normalize=True).plot(kind='bar',xlabel='Type of use',ylabel='Total exposure',ax=axes[0,3])
data.fleetc.value_counts(normalize=True).plot(kind='bar',xlabel='Fleet or not',ylabel='Total exposure',ax=axes[0,4])
data.AGEPH.plot(kind='hist',xlabel='Age',ylabel='Total exposure',bins=40,weights=np.ones(len(data)) / len(data),ax=axes[1,0])
data.powerc.value_counts(normalize=True).plot(kind='bar',xlabel='Power of car',ylabel='Total exposure',ax=axes[1,1])
data.agecar.value_counts(normalize=True).plot(kind='bar',xlabel='Age of car',ylabel='Total exposure',ax=axes[1,2])
data.sportc.value_counts(normalize=True).plot(kind='bar',xlabel='Sports car or not',ylabel='Total exposure',ax=axes[1,3])
data.split.value_counts(normalize=True).plot(kind='bar',xlabel='Split of premium',ylabel='Total exposure',ax=axes[1,4])
fig.suptitle('Risk factors')

fig, axes = plt.subplots(nrows=2, ncols=5)
plt.figure(3)
# info policy holders
data.groupby(['coverp'])['nbrtotp'].mean().plot(kind='bar',xlabel='Type of coverage',ylabel='Average nb claims',ax=axes[0,0])
data.groupby(['fuelc'])['nbrtotp'].mean().plot(kind='bar',xlabel='Type of fuel',ylabel='Average nb claims',ax=axes[0,1])
data.groupby(['sexp'])['nbrtotp'].mean().plot(kind='bar',xlabel='Sex',ylabel='Average nb claims',ax=axes[0,2])
data.groupby(['usec'])['nbrtotp'].mean().plot(kind='bar',xlabel='Type of use',ylabel='Average nb claims',ax=axes[0,3])
data.groupby(['fleetc'])['nbrtotp'].mean().plot(kind='bar',xlabel='Fleet or not',ylabel='Average nb claims',ax=axes[0,4])
data.groupby(['AGEPH'])['nbrtotp'].mean().plot(kind='line',xlabel='Age ph',ylabel='Average nb claims',ax=axes[1,0])
data.groupby(['powerc'])['nbrtotp'].mean().plot(kind='bar',xlabel='Power of car',ylabel='Average nb claims',ax=axes[1,1])
data.groupby(['agecar'])['nbrtotp'].mean().plot(kind='bar',xlabel='Age of car',ylabel='Average nb claims',ax=axes[1,2])
data.groupby(['sportc'])['nbrtotp'].mean().plot(kind='bar',xlabel='Sports car or not',ylabel='Average nb claims',ax=axes[1,3])
data.groupby(['split'])['nbrtotp'].mean().plot(kind='bar',xlabel='Split of premium',ylabel='Average nb claims',ax=axes[1,4])
fig.suptitle('Risk factors')

shp.plot(column='duree',cmap='jet',legend=True)
shp.plot(column='mean_nbrtotp',cmap='jet',legend=True)

plt.show()