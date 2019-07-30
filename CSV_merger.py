import glob
import pandas as pd
import numpy as np

 
#path to directory which contains csv files
path = r'/path/'

allFiles = glob.glob(path+'\*.csv')

dataset = pd.DataFrame()

for f in allFiles:

    hold = pd.read_csv(f)

    dataset = pd.concat([dataset,hold ], axis=0)

dataset.to_csv('output.csv', index=False)
