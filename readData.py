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


def split_to_numeric(x):
    if x == 'Once': return 0
    if x == 'Twice': return 1
    if x == 'Thrice': return 2
    return 3


def agec_to_numeric(x):
    if x == '2-5': return 1
    if x == '6-10': return 2
    if x == '>10': return 3
    return 0


def powerc_to_numeric(x):
    if x == '66-110': return 1
    if x == '>110': return 2
    return 0


def sexp_to_numeric(x):
    if x == 'Male': return 1
    return 0


def fuelc_to_numeric(x):
    if x == 'Gasoil': return 1
    return 0


def usec_to_numeric(x):
    if x == 'Professional': return 1
    return 0


def fleetc_to_numeric(x):
    if x == 'Yes': return 1
    return 0


def sportc_to_numeric(x):
    if x == 'Yes': return 1
    return 0


def coverp_to_numeric(x):
    if x == 'MTPL+': return 1
    if x == 'MTPL+++': return 2
    return 0


data = pd.read_csv('Assignment.csv')
postalData = pd.read_excel('inspost.xls')
data = pd.merge(data, postalData)
data['chargper'] = np.where(data['nbrtotc'] > 0, data.chargtot / data.nbrtotc, 0)

dataFact = pd.DataFrame()
dataFact['ageph'] = data.AGEPH
dataFact['duree'] = data.duree
dataFact['lnexpo'] = data.lnexpo
dataFact['nbrtotc'] = data.nbrtotc
dataFact['chargtot'] = data.chargtot
dataFact['chargper'] = data.chargper
dataFact['agecar'] = data.agecar.apply(agec_to_numeric)
dataFact['sexp'] = data.sexp.apply(sexp_to_numeric)
dataFact['fuelc'] = data.fuelc.apply(fuelc_to_numeric)
dataFact['split'] = data.split.apply(split_to_numeric)
dataFact['usec'] = data.usec.apply(usec_to_numeric)
dataFact['fleetc'] = data.fleetc.apply(fleetc_to_numeric)
dataFact['sportc'] = data.sportc.apply(sportc_to_numeric)
dataFact['coverp'] = data.coverp.apply(coverp_to_numeric)
dataFact['powerc'] = data.powerc.apply(powerc_to_numeric)
dataFact['lat'] = data.LAT
dataFact['long'] = data.LONG

data.to_csv(r'./data.csv', encoding='utf-8', index=False)
dataFact.to_csv(r'./dataFact.csv', encoding='utf-8', index=False)