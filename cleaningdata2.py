import csv
import pandas as pd

data = pd.read_csv('dwarfplanets.csv', encoding= 'unicode_escape')
data = data.dropna()

data.loc[:,'RADIUS'] *= 0.102763
data.loc[:, 'MASS'] *= 0.000954588

data.to_csv('dwarfplan2.csv', index = False)
print(data)