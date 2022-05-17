import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)
import pickle

data_frame = pd.read_csv(
    "TestData//Test1_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]

filename = 'rbf_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result1 = loaded_model.predict(data_features)

count = 0 
for i in range(len(result1)):
    if int(result1[i]) == int(data_labels[i]):
        count+=1

print("Test File Test1_MeanData_ML with Random Forest model: %.2f%% " % ((count/len(data_labels))*100))

data_frame = pd.read_csv(
    "TestData//Test2_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]
result2 = loaded_model.predict(data_features)

count = 0 
for i in range(len(result1)):
    if int(result2[i]) == int(data_labels[i]):
        count+=1

print("Test File Test2_MeanData_ML with Random Forest model: %.2f%% " % ((count/len(data_labels))*100))