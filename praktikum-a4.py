nim = ['2','3','1','0','3','1','0','2','6']
# nim2 =  '231031026'
print(nim[1:3])
# print(nim2[1:3])

# akses item 
print(f'item indeks 0:{nim[0]}')
print(f'item indeks 4:{nim[4]}')
print(f'item indeks terakhir : {nim[len(nim)-1]}')

# akses indeks negatif
print(f'item indeks terakhir : {nim[-1]}')
print(f'item indeks pertama : {nim[-len(nim)]}')
print(f'item indeks 6 [-3] : {nim[-3]}')
print(f'item indeks 4 [-5] : {nim[-5]}')
print(f'item indeks 7 [-2] : {nim[-2]}')

# akses indeks batas 
print(f'item index 1,2,....: \n {nim[1:]}\n')
print(f'item index 3,4,....: \n {nim[3:]}')
print(f'item index 0,1,2...: \n {nim[:3]}')
print(f'item index 0,1,2,3.: \n {nim[:4]}')
print(f'item index semua...: \n {nim[:]}')
print(f'item index [:8] : \n {nim[:-1]}')
print(f'item index [:6] : \n {nim[:-3]}')

# pengirisan 
print(f'item index 1,2 : \n {nim[1:3]}')
print(f'item index 2,3,4 : \n {nim[2:5]}')
print(f'item index kosong : \n {nim[3:3]}')
print(f'item index [8:8] kosong : \n {nim[-1:-1]}')
print(f'item index [1:8] : \n {nim[1:-1]}')
print(f'item index [2:7] : \n {nim[2:-2]}')


# latihan list
print('\nlatihan list', '='*20)
data = ['Fadhil Aditya', 2023, 'aktif']
nilai = [98, 97, 96, 95]

print(f'Nama : {data[0]} status kuliah : {data[2]}\n')
print(f'Data tebesar nilai adalah : {max(nilai)}\n')
print(f'Data terkecil nilai adalah : {min(nilai)}\n')
print(f'rata-rata nilai nilai adalah : {sum(nilai)/len(nilai)}\n')


# latihan tuple
print('latihan tuple', '='*20)
data = ('Fadhil Aditya', 2023, 'aktif')
nilai = (98, 97, 96, 95)

print(f'Jumlah nilai mahasiswa adalah {len(nilai)}\n')
print(f'Data tebesar nilai adalah : {max(nilai)}\n')
print(f'Data terkecil nilai adalah : {min(nilai)}\n')
print(f'rata-rata nilai nilai adalah : {sum(nilai)/len(nilai)}')


# latihan nested list

print('latihan nested list', '='*20)
data = [['Fadhil Aditya', 2023, 'Aktif'],
        [98, 97, 96, 95],
        [20, 22],
        ['S1-Reguler', 'Ganjil']
     ]

matkul = ['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ']
sks    = [2,2,2,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata kuliah 1: {data[-2][0]} dengan jumlah {data[-1][0]} sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'Mata kuliah 2: {data[-2][1]} dengan jumlah {data[-1][1]} sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'Mata kuliah 3: {data[-2][2]} dengan jumlah {data[-1][2]} sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'Mata kuliah 4: {data[-2][3]} dengan jumlah {data[-1][3]} sks\n')
data[-2].append('Pengantar Pemrograman')
data[-1].append(3)
# print(data)
# Tambahkan 3 matkul dengan sks nya
data[-2].append('Pengantar Teknologi Informasi')
data[-1].append(3)
data[-2].append('Kalkulus Dasar 1')
data[-1].append(3)
data[-2].append('Sains Terpadu')
data[-1].append(3)
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Mata kuliah 6: {data[4][4]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Mata kuliah 7: {data[4][5]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'Mata kuliah 8: {data[4][6]} dengan jumlah {data[-1][6]} sks\n')

# Tambahkan 8 nilai masing-masing
data[1].append(98)
data[1].append(96)
data[1].append(95)
data[1].append(90)

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
print(f'\nNama Mahasiswa {data[0][0]} dengan NIM {"".join(nim)}\n')
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[-3][0]}\n')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[-3][1]}\n')
# >> Jumlah nilai Thomas adalah: 8
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}\n')
# >> Data terbesar Thomas adalah: 98
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}\n')
# >> Data terkecil Thomas adalah: 90
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}\n')
# >> Rata-rata nilai Thomas adalah: 94.625
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/(len(data[1]))}')