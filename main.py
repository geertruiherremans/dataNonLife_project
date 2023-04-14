"""
Tariff plan construction using:
- GAM
- Gradient boosting
"""
import pandas as pd
from pygam import PoissonGAM, s, f
import numpy as np
import math
import matplotlib.pyplot as plt
import geopandas as gpd

data = pd.read_csv('data.csv')
data['sex'] = data.sexp == 'Male'
data.sex = data['sex'].astype(int)
y = data.nbrtotc.to_numpy()
X = data[['AGEPH','sex']].to_numpy()
gamTest = PoissonGAM(s(0)+f(1)).fit(X,y,exposure=data.duree)
gamTest.summary()