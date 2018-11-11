nama = input('Masukan Nama  ')
usia = input('Masukan Usia  ')
usia = int(usia) # konversi string menjadi integer
if usia >= 65:
    kategori = 'Lansia'
elif usia >= 25:
    kategori = 'Dewasa'
elif usia >= 17:
    kategori = 'Remaja'
elif usia >= 13:
    kategori = 'Remaja'
elif usia >= 6:
    kategori = 'Anak-anak'
elif usia >= 1:
    kategori = 'Balita'
else:
    kategori = 'Bayi'

print('{} Tergolong {}'.format(nama,kategori))
