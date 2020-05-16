import pandas as pd
import numpy as np
import seaborn as sns


#регулируем настройки экрана для отчета
pd.set_option("display.width", 200)
pd.set_option('display.max_columns', None)

#загружаем данные
data = pd.read_csv('./data.csv')

#print(data.head())

#print(data.dtypes)

#print(data.shape)


#print(data.isnull().sum())

#количество нулевых значений
print(data['inspection_score'].isna().sum())

mean = data['inspection_score'].mean()

data['inspection_score'].fillna(mean, inplace=True)
print(data['inspection_score'].isna().sum())

print(data['risk_category'].isna().sum())


data['risk_category'].isna().sum()
#print(data['Research'].isna().sum())

data = data[~data['risk_category'].isna()]


print(data['risk_category'].isna().sum())

ax = sns.violinplot(x=data['inspection_score'])