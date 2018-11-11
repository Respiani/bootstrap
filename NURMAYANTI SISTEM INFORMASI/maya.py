elif usia >= 17:
	kategori = 'pemuda'
elif usia >= 13:
	kategori = 'remaja'
elif usia >= 6:
	kategori = 'anak-anak'
elif usia >= 1:
	kategori = 'balita'
else:
	kategori = 'bayi'
print('{} tergolong {}'.format(nama,kategori))