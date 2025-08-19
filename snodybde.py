import pandas as pd # lese data fra excel-fil og bruke DataFrames
import seaborn as sns # plotting
sns.set(style = 'whitegrid', font_scale = 1.5) # utseende av plott
import matplotlib.pyplot as plt # og mer plotting
import numpy as np # matematikk
import statistics  # statistikk-funksjoner

snodybde = pd.read_excel('snodybde_1516.xlsx') # leser inn excel-fila
snodybde.shape # dimensjonen på datasettet
print(snodybde)

print(f"Gjennomsnittet er {statistics.mean(snodybde['Snødybde']):.2f} cm")
print(f"Standardavviket er {statistics.stdev(snodybde[ 'Snødybde' ] )}")
print(f"Medianen er {statistics.median(snodybde[ 'Snødybde' ])}")
print(f"Kvartilbredden er {np.quantile(snodybde['Snødybde'], 0.75) - np.quantile(snodybde['Snødybde'], 0.25)} ")
print(f"Variasjonsbredden er {max(snodybde['Snødybde']) - min(snodybde['Snødybde'])}")

antall, intervaller = np.histogram(snodybde['Snødybde'], bins = range(0,80,10))
tabell = {'Intervaller' : ['[0-10 cm)','[10-20 cm)','[20-30 cm)','[30-40 cm)',
                         '[40-50 cm)','[50-60 cm)','[60-70 cm)'],
          'Antall dager' : antall}

# Lager en pandas DataFrame
tabelldf = pd.DataFrame(tabell, columns = ['Intervaller','Antall dager'])
print(tabelldf)

# Regner ut andeler
tabelldf['Andel dager'] = round(tabelldf['Antall dager']/sum(tabelldf['Antall dager']),3)
print(tabelldf)

# Plotter et histogram av observasjonene
sns.histplot(snodybde['Snødybde'],bins = range(0,80,10))
plt.show()

# Plotter et histogram av observasjonene der tellingene (Count) er skalert slik at areal under stolpene er 1
sns.histplot(snodybde['Snødybde'],bins = range(0,80,10), stat="density")
plt.show()

# Plotter et boksplott av observasjonene
sns.boxplot(y='Snødybde',data=snodybde)
plt.show()