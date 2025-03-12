import pandas as pd
import matplotlib.pyplot as plt

eggplants = pd.read_csv('/Users/griffinkeeler/Desktop/VscodePy/report.csv')

eggplants.head(5)

columns_to_add = ['Date', 'Weighted Avg Price']
eggplants = eggplants.loc[:, columns_to_add]

print(eggplants)

month = pd.DatetimeIndex(eggplants['Date']).month

new_eggplants = pd.DataFrame({'Month': month, 'Price': eggplants['Weighted Avg Price'] })
print(new_eggplants)

month = new_eggplants.Month
price = new_eggplants.Price



new_eggplants.groupby(['Month'])['Price'].mean().plot(kind='bar')
plt.ylabel('Eggplant Price')


plt.show()
