"""
Tariff plan construction using:
- GAM
- Gradient boosting
"""
import pandas as pd
from pygam import PoissonGAM, s, f, te
import numpy as np
import math
import matplotlib.pyplot as plt
import geopandas as gpd
from scipy.interpolate import interp1d


data = pd.read_csv('dataFact.csv')
y = data.nbrtotc.to_numpy()
X = data[['ageph','sexp','coverp','fuelc','lat','long']].to_numpy()
gamTest = PoissonGAM(s(0)+f(1)+f(2)+f(3)+te(4,5)).fit(X,y,exposure=data.duree)
gamTest.summary()

postalData = pd.read_excel('inspost.xls')
postalData = postalData.sort_values(by='CODPOSS')
coord = postalData[['LAT','LONG']].to_numpy()
XX = np.concatenate((np.zeros((coord.shape[0],4)),coord),axis=1)
YY = gamTest.predict(XX)
postalData['YY'] = YY
postalData = postalData.rename(columns={'CODPOSS':'POSTCODE'})
shp = gpd.read_file(r'./shape_file/npc96_region_Project1.shp')
shp = shp.sort_values(by='POSTCODE')
shp.YY = shp.YY.fillna(0)

shp.plot(column='duree',cmap='jet',legend=True)