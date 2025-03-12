import matplotlib.pyplot as plt
import numpy as py
from sklearn import datasets, linear_model, model_selection
from sklearn.datasets import load_linnerud

linnerud = load_linnerud()

X = linnerud.data
y = linnerud.target


X_test, X_train, y_test, y_train = model_selection.train_test_split(X, y, test_size=0.2)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(X)
print(y)
plt.scatter(X_test, y_test, color='black')
# plt.plot(X_test, y_pred, color='red', linewidth = 3)
plt.show()



