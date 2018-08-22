import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import sys

plt.rc("font", size=14)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


data = pd.read_csv('Model-python.csv', engine = 'python', encoding = "latin-1")

# List of data columns
print(list(data.columns))
# Number of rows and columns before dropping N/A values
print("Before dropping N/A values: " + str(data.shape))

# Drop all N/A values from data set
data = data.dropna()

print("After dropping N/A values: " + str(data.shape))

# Barplot for the dependent variable - employment status
sns.countplot(x = 'Employment Status', data = data, palette='hls')
plt.show()
sns.countplot(y = 'Job Title', data = data)
plt.show()
sns.countplot(y = 'Division', data = data)
plt.show()
col_names_for_dummies = list(data.columns).remove("Employment Status")


data2 = pd.get_dummies(data, columns = col_names_for_dummies)
#print(list(data2.columns))

sns.heatmap(data2.corr())
plt.show()

# Splitting data into training and evaluation sets
# In each iloc specification, the first part is for all rows and the second part is for columns
# Column[0] is the employement status - to be predicted and all the others are independent variables
X = data2.iloc[:, 1:]
y = data2.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = None)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
#print(data)

classifier = LogisticRegression(random_state=0)
print(classifier.fit(X_train, y_train))

y_pred = classifier.predict(X_test)

confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
