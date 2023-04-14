
import pandas as pd
import numpy as np

data = pd.read_csv('Assignment.csv')
postalData = pd.read_excel('inspost.xls')
nData = data.shape[0]

for iDat in range(nData):
    ind = postalData[postalData['CODPOSS']==data.loc[iDat,'CODPOSS']].index.values
    data.loc[iDat,'LAT'] = postalData.loc[ind,'LAT'].values
    data.loc[iDat,'LONG'] = postalData.loc[ind,'LONG'].values

data.to_csv(r'./data.csv', encoding='utf-8',index=False)

print(data['LAT'].isin([0]).any())
print(data['LONG'].isin([0]).any())
