import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snsc

df = pd.read_csv('d:/Exercices- projet  Python/Mini projet python/Donnees_ventes.csv', encoding='latin1')

print("Dimensions des données :", df.shape)

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df = df.fillna(0)

#print("\nValeurs manquantes après remplacement :")
#print(df.isnull().sum())

df_selected = df[['SALES', 'QUANTITYORDERED']]

df_filtered = df[df['SALES'] > 3000]
df_filtered = df[df['QUANTITYORDERED'] < 35]


df['vente_globale'] = df['SALES'] * df['QUANTITYORDERED']
print(df.head())

print("Données avant tri: ")
print(df[['SALES']].head())

df_sorted = df.sort_values('SALES', ascending=False)

print("\n Données après tri (SALES décroissant): ")
print(df_sorted[['SALES']].head())

print("Moyenne SALES :", df['SALES'].mean())
print("Médiane SALES :", df['SALES'].median())
print("Écart-type SALES :", df['SALES'].std())

print("Moyenne QUANTITYORDERED :", df['QUANTITYORDERED'].mean())
print("Médiane QUANTITYORDERED :", df['QUANTITYORDERED'].median())
print("Écart-type QUANTITYORDERED :", df['QUANTITYORDERED'].std())

df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')
df_grouped = df.groupby('DEALSIZE')['SALES'].agg(['mean', 'sum', 'count'])
print(df_grouped)

df_grouped = df.groupby('TERRITORY')['CONTACTLASTNAME'].agg(['count', 'nunique'])
print(df_grouped)


df['SALES'].plot(kind='hist', bins=20)
plt.title('Distribution de SALES')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.show()

sales_by_year = df.groupby('YEAR_ID')['SALES'].sum().reset_index()

sales_by_year.plot(x='YEAR_ID', y='SALES', kind='hist', legend=False)
plt.title('Total des ventes par ID année')
plt.xlabel('ID_Année')
plt.ylabel('Total des ventes')
plt.tight_layout()
plt.show()

df.groupby('SALES')['vente_globale'].sum().plot()
plt.title('Évolution des vente_globale / Sales')
plt.ylabel('Vente globale')
plt.show()

df.groupby('QUANTITYORDERED')['SALES'].sum().plot()
plt.title('Évolution des ventes en fonction des quantités commandées')
plt.ylabel('Ventes')
plt.show()


df.boxplot(column='SALES', by='QUANTITYORDERED')
plt.title('\n Boxplot de SALES par QUANTITYORDERED')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

