#krok 1 import klas i modułów
import numpy as np
from sklearn.linear_model import LinearRegression

#krok 2 podanie danych

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

#krok 3 stworzenie modelu i fit it
model = LinearRegression()

model.fit(x, y)

model = LinearRegression().fit(x, y)

#krok 4 get results

r_sq = model.score(x, y)

print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)

print('slope:', model.coef_)

new_model = LinearRegression().fit(x, y.reshape((-1, 1)))

print('intercept:', new_model.intercept_)

print('slope:', new_model.coef_)

#krok 5 predict response

y_pred = model.predict(x)

print('predicted response:', y_pred, sep='\n')

y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)

print('predicted response:', y_pred, sep='\n')
