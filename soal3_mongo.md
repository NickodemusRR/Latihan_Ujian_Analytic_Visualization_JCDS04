# Membuat database menggunakan MongoDB

Mengaktifkan server MongoDB
```bash
C:\Program Files\MongoDB\Server\4.0\bin>mongod
```

Menjalankan program MongoDB
```bash
C:\Program Files\MongoDB\Server\4.0\bin>mongo
```

1. Membuat database baru dan menggunakannnya.
```bash
> use Kampus
switched to db Kampus
```

2. Membuat user baru bernama Andi sebagai _admin_ dan Budi yang mampu membaca dan menulis ke database tetapi bukan _admin_.
```bash
> db.createUser({
... user:'andi',
... pwd:'anditopsecret',
... roles:['readWrite', 'dbAdmin']
... })
Successfully added user: { "user" : "andi", "roles" : [ "readWrite", "dbAdmin" ] }
> db.createUser({
... user:'budi',
... pwd:'buditopsecret',
... roles:['readWrite']
... })
Successfully added user: { "user" : "budi", "roles" : [ "readWrite" ] }
```

3. Membuat dan memasukkan data ke collection __Dosen__
```bash
> db.Dosen.insertMany([ 
    {nama:'Caca', usia:28, asal:'Jakarta', bidang:'Fisika Astrologi', titel:'S2', status:'Honorer', nip:123, matkul:['Metrologi', 'Kosmologi', 'Kalkulus']}, 
    {nama:'Dedi', usia:29, asal:'Yogyakarta', bidang:'Fisika Terapan', titel:'S3', status:'PNS', nip:456, matkul:['Instrumentasi', 'Elektronika', 'Fisika Dasar']},
     {nama:'Euis', usia:30, asal:'Bandung', bidang:'Fisika Teoretik', titel:'S1', status:'Honorer', nip:789, matkul:['Fisika Dasar', 'Fisika Modern', 'Kalkulus']}
    ])
```

4. Membuat dan memasukkan data ke collection __Mahasiswa__
```bash
> db.Mahasiswa.insertMany([
... {nama:'Faza', usia:19, asal:'Aceh', prodi:'Fisika', angkatan:2017, nim:123},
... {nama:'Gilang', usia:20, asal:'Semarang', prodi:'Fisika', angkatan:2017, nim:456},
... {nama:'Hanafi', usia:19, asal:'Makassar', prodi:'Fisika', angkatan:2017, nim:789}
])
```