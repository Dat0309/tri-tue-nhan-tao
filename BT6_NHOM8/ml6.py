from re import M
import pandas as pd
import numpy as np
from sklearn.svm import SVC

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from numpy import mean
from numpy import std
import pickle

data_frame = pd.read_csv(
    "Training_MeanData_ML.csv")

data_features = data_frame.values[:,1:-1]
data_labels = data_frame.values[:,-1]

data_features = np.array(data_features)
print(data_features)

train_set, test_set = train_test_split(data_frame, test_size=0.2)

print(len(train_set))
print(len(test_set))

x_train = train_set.values[:,1:-1]
y_train = train_set.values[:,-1]
x_test = test_set.values[:,1:-1]
y_test = test_set.values[:, -1]

# model = SVC(kernel='rbf', random_state = 1)
# model.fit(x_train, y_train)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 100)
cv = KFold(n_splits=10, random_state=1, shuffle=True)
regressor.fit(x_train, y_train)
scores = cross_val_score(regressor, data_features, data_labels, cv=cv, n_jobs=-1)
print(scores)
print("Train: %.2f%% " % (mean(scores)*100))

# save the model to disk
filename = 'RFR_model.sav'
pickle.dump(regressor, open(filename, 'wb'))
print('save model completed')

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(x_test, y_test)
print("Test: %.2f%% " % ((result)*100))