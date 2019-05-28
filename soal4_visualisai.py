import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# buat dataframe dengan membaca file csv
df_bcg = pd.read_csv('./Balita Terimunisasi BCG 1995-2017.csv', na_values='n.a')
df_campak = pd.read_csv('./Balita Terimunisasi Campak 1995-2017.csv', na_values='n.a')
df_dpt = pd.read_csv('./Balita Terimunisasi DPT 1995-2017.csv', na_values='n.a')
df_polio = pd.read_csv('./Balita Terimunisasi Polio 1995-2017.csv', na_values='n.a')

# interpolasi data yang tidak ada dengan method .interpolate()
# menghitung jumlah balita yang belum mendapat imunisasi
df_bcg = df_bcg.interpolate()
df_bcg['% Balita yang tidak mendapat imunisasi BCG'] = 100 - df_bcg['% Balita yang pernah mendapat imunisasi BCG']
# print(df_bcg)

df_campak = df_campak.interpolate()
df_campak['% Balita yang tidak mendapat imunisasi Campak'] = 100 - df_campak['% Balita yang pernah mendapat imunisasi Campak']

df_dpt = df_dpt.interpolate()
df_dpt['% Balita yang tidak mendapat imunisasi DPT'] = 100 - df_dpt['% Balita yang pernah mendapat imunisasi DPT']

df_polio = df_polio.interpolate()
df_polio['% Balita yang tidak mendapat imunisasi Polio'] = 100 - df_polio['% Balita yang pernah mendapat imunisasi Polio']

sns.set(style="whitegrid")

# Plot Figure 1: Persentase balita terimunisasi 1995 - 2017
plt.figure('Persentase balita terimunisasi 1995-2017', figsize=(10,8))
plt.subplot(221)
sns.barplot(x='Tahun', y='% Balita yang pernah mendapat imunisasi BCG', data=df_bcg, color='blue')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('BCG')
plt.subplot(222)
sns.barplot(x='Tahun', y='% Balita yang pernah mendapat imunisasi Campak', data=df_campak, color='red')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('Campak')
plt.subplot(223)
plt.xticks(rotation=60)
sns.barplot(x='Tahun', y='% Balita yang pernah mendapat imunisasi DPT', data=df_dpt, color='green')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('DPT')
plt.subplot(224)
sns.barplot(x='Tahun', y='% Balita yang pernah mendapat imunisasi Polio', data=df_polio, color='yellow')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('Polio')
plt.tight_layout()

# Plot Figure 2: Persentase balita terimunisasi 1995 - 2017
plt.figure('Persentase balita tidak terimunisasi 1995-2017', figsize=(10,8))
plt.subplot(221)
sns.barplot(x='Tahun', y='% Balita yang tidak mendapat imunisasi BCG', data=df_bcg, color='blue')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('BCG')
plt.subplot(222)
sns.barplot(x='Tahun', y='% Balita yang tidak mendapat imunisasi Campak', data=df_campak, color='red')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('Campak')
plt.subplot(223)
plt.xticks(rotation=60)
sns.barplot(x='Tahun', y='% Balita yang tidak mendapat imunisasi DPT', data=df_dpt, color='green')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('DPT')
plt.subplot(224)
sns.barplot(x='Tahun', y='% Balita yang tidak mendapat imunisasi Polio', data=df_polio, color='yellow')
plt.xticks(rotation=60)
plt.ylabel('')
plt.title('Polio')
plt.tight_layout()

plt.show()