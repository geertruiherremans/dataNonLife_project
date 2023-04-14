"""
Preprocessing of data
Converting input data 'Assignment.csv' to 'data.csv' (used in main)
- Postal code converted to latitude and longitude
- Additional column: chargper = claim amount per claim
"""
import pandas as pd
import numpy as np

data = pd.read_csv('Assignment.csv')
postalData = pd.read_excel('inspost.xls')
data = pd.merge(data,postalData)
data['chargper'] = np.where(data['nbrtotc']>0,data.chargtot / data.nbrtotc,0)

data.to_csv(r'./data.csv', encoding='utf-8',index=False)

