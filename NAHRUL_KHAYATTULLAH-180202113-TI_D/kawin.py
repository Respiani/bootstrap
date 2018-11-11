nama = input('Masukan nama Anda : ')
usia = input('masukan Usia Anda : ')
kawin = input('Udah kawin belom?  ya/tidak ')

if kawin=='ya' or int(usia) >=17:
    print('{} Sudah bisa mencoblos pada pemilu'.format(nama))
else:
    print('{} Belum bisa Nyoblos'.format(nama))
