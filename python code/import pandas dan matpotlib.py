import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv('company_sales_data.csv')

print(df["facecream"].tolist())

df.set_index('facecream').plot()

plt.show()

