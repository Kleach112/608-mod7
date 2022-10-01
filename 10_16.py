# 10.16 Linear Regression - Kim Leach

c = lambda f: 5 / 9 * (f - 32)

temps = [(f, c(f)) for f in range(0, 101, 10)]

import pandas as pd

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])

axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')

y_label = axes.set_ylabel('Celsius')

# Kim Leach

# creating a DataFrame
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')

nyc.head()

nyc.tail()

nyc.columns = ['Date', 'Temperature', 'Anomaly']

nyc.head(3)

nyc.Date.dtype

nyc.Date = nyc.Date.floordiv(100)

nyc.head(3)

pd.set_option('display.precision', 2)

nyc.Temperature.describe()

from scipy import stats

linear_regression = stats.linregress(x=nyc.Date,
                                     y=nyc.Temperature)

linear_regression.slope

linear_regression.intercept

linear_regression.slope * 2019 + linear_regression.intercept

linear_regression.slope * 1850 + linear_regression.intercept

import seaborn as sns

sns.set_style('whitegrid')

axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)

axes.set_ylim(10, 70)


year = 2019

slope = linear_regression.slope

intercept = linear_regression.intercept

temperature = slope * year + intercept

while temperature < 40.0:
    year += 1
    temperature = slope * year + intercept

year