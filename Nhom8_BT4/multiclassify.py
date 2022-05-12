import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC

X = pd.read_csv('Training_Data_ML.csv')
a = np.array(X)
Y = a[:,6]

print (X), (Y)

clf = SVC(kernel='linear')

clf.fit(X,Y)

clf.predict([[-73, -53]]) 
clf.predict([[-73, -46]])
print('done')