import pandas as pd # lese data fra csv-fil
import seaborn as sns # plotting
sns.set(style = 'whitegrid', font_scale = 1.5) # utseende av plott
import matplotlib.pyplot as plt # og mer plotting
import numpy as np # matematikk

df = pd.read_csv('personbildata.csv', index_col=0) # lese inn datasettet (cvs-fil med radnavn)
df.shape  # Dimensjonen til datasettet
print(df)

df2020 = df.iloc[12,].to_frame().transpose()  # Hente ut rad 12 (2020) til ny pandas DataFrame
print(df2020)

df2020 = df2020.div(df2020.sum(axis=1),axis=0) # Bytte ut antall med andel
print(df2020)

palette = sns.color_palette(["#d55e00","#0072b2","#009e73", "#f0e442"])
# palette = farger for de fire drivstoff-kategoriene
# Har hentet fargeblind-vennlige palett fra https://www.color-hex.com/color-palette/49436

sns.barplot(data = df2020, palette = palette)
# Plotter et enkelt stolpediagram (barplot) med Seaborn-modulen
plt.show()

df2020sort = df2020.sort_values(by = 2020,axis=1,ascending=False)
# Sorterer dataene fra største til minste andel
print(df2020sort)

# Plotter de sorterte dataene (og sorterer fargene)
palette_sort = sns.color_palette(["#0072b2","#d55e00","#009e73", "#f0e442"])

sns.barplot(data = df2020sort,palette = palette_sort)
plt.show()

df_andel = df.div(df.sum(axis=1),axis=0) # Lager et datasett med årlige andeler i stedet for antall

# Plotter utvikling i andeler av hver kategori med et Seaborn lineplot
sns.lineplot(data = df_andel,palette = palette)
plt.ylim(0,1); plt.xlim(2008,2020)
plt.show()