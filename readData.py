"""
Preprocessing of data
Converting input data 'Assignment.csv' to 'data.csv' (used in main)
- Postal code converted to latitude and longitude
- Additional column: chargper = claim amount per claim
Converting input data to 'dataFact.csv' (used in main)
- All categorical data is converted to factorial data
- Used as input for GAM
"""
import pandas as pd
import numpy as np


data = pd.read_csv('Assignment.csv')
postalData = pd.read_excel('inspost.xls')
data = pd.merge(data, postalData)
data['chargper'] = np.where(data['nbrtotc'] > 0, data.chargtot / data.nbrtotc, 0)

data.to_csv(r'./data.csv', encoding='utf-8', index=False)


data['agecar'] = data['agecar'].map({'0-1':0, '2-5':1, '6-10':2,'>10':3})
data['sexp'] = data['sexp'].map({'Male':0,'Female':1})
data['fuelc'] = data['fuelc'].map({'Gasoil':1,'Petrol':0})
data['split'] = data['split'].map({'Once':0,'Twice':1,'Thrice':2,'Monthly':3})
data['usec'] = data['usec'].map({'Private':0,'Professional':1})
data['fleetc'] = data['fleetc'].map({'No':0,'Yes':1})
data['sportc'] = data['sportc'].map({'No':0,'Yes':1})
data['coverp'] = data['coverp'].map({'MTPL':0,'MTPL+':1,'MTPL+++':2})
data['powerc'] = data['powerc'].map({'<66':0,'66-110':1,'>110':2})

data.to_csv(r'./dataFact.csv', encoding='utf-8', index=False)