import csv
import pandas as pd
dataset=pd.read_csv('final_dataset.csv')
print "Seeing the trend in the dataset";
print dataset.describe()
print "Observing the NaN values in the dataset"
print dataset.info()

#Printing the heatmap

import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
sns.set(style="ticks",color_codes=True)

print "Printing the heatmap to analyse correlation among features"

plt.subplots(figsize=(40,40))
ax=subplots(111);
sns.heatmap(dataset.corr(),linewidths=0.5,square=True,linecolor='white',annot=True,ax=ax)
plt.show()

print "The heatmap shows the strong relation between kingvist garden knighthouse capital"

corr_list=dataset.astype(float).corr()['price'].sort_values(ascending=False)

print "The correlation list of features with label"
print corr_list