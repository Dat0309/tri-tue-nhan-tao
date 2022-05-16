import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)
import pickle

data_frame = pd.read_csv(
    "TestData//Test1_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]

filename = 'RFR_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result1 = loaded_model.score(data_features, data_labels)
print("Test File Test1_MeanData_ML with Random Forest model: %.2f%% " % ((result1)*100))

data_frame = pd.read_csv(
    "TestData//Test2_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]

filename = 'RFR_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result2 = loaded_model.score(data_features, data_labels)
print("Test File Test2_MeanData_ML with Random Forest model: %.2f%% " % ((result2)*100))

print("Test ratio model with random forest: %.2f%% " % (((result1+result2)/2)*100))

data_frame = pd.read_csv(
    "TestData//Test1_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]

filename = 'rbf_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result3 = loaded_model.score(data_features, data_labels)
print("Test File Test2_MeanData_ML with RBF model: %.2f%% " % ((result3)*100))

data_frame = pd.read_csv(
    "TestData//Test2_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]

filename = 'rbf_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result4 = loaded_model.score(data_features, data_labels)
print("Test File Test2_MeanData_ML with RBF model: %.2f%% " % ((result4)*100))

print("Test ratio model with RBF: %.2f%% " % (((result3+result4)/2)*100))