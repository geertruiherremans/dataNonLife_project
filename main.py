"""
Tariff plan construction using:
- GAM
- Gradient boosting
"""
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import geopandas as gpd

data = pd.read_csv('data.csv')
dataSev = data[data.nbrtotc!=0]