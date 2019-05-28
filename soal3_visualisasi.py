import pandas as pd 
import matplotlib.pyplot as plt 
from pymongo import MongoClient

server = MongoClient('mongodb://localhost:27017/')

db = server['Kampus']        # mengakses database
col1 = db['Dosen']          # masuk ke collection yang ada di database
col2 = db['Mahasiswa']

dfdosen = pd.DataFrame(list(col1.find()))
dfdosen['status'] = 'dosen'
dfdosen = dfdosen[['asal', 'nama', 'status', 'usia']]

dfmahasiswa = pd.DataFrame(list(col2.find()))
dfmahasiswa['status'] = 'mahasiswa'
dfmahasiswa = dfmahasiswa[['asal', 'nama', 'status', 'usia']]

plt.bar(dfdosen['nama'], dfdosen['usia'], color='red')
plt.bar(dfmahasiswa['nama'], dfmahasiswa['usia'], color='blue')
plt.title('Usia Warga Kampus')
plt.legend(['Dosen', 'Mahasiswa'])
plt.grid()

plt.show()