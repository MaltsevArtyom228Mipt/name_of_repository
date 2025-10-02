import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

species_counts = df['Species'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Распределение по видам')
plt.show()

bins = [0, 1.2, 1.5, df['PetalLengthCm'].max()]
labels = ['<=1.2 cm', '1.2-1.5 cm', '>1.5 cm']
df['petal_category'] = pd.cut(df['PetalLengthCm'], bins=bins, labels=labels, include_lowest=True)

petal_counts = df['petal_category'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(petal_counts, labels=petal_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Категории длины петли')
plt.show()