print('praktikum-a2\n')

print('NAMA     : FADHIL ADITYA')
print('NIM      : 231031026')
print('Prodi    : Sistem Informasi A\n')

# INI OPERATOR  ASSIGMENT
a = 19
print('nilai a adalah', a)

a += 3
print('nilai a+=  adalah', a)

a = 19
print('nilai a adalah', a)

a -= 3
print('nilai a-= adalah', a)

a = 19
print('nilai a adalah', a)

a *= 2
print('nilai a*=2 adalah', a)

a = 19
print('nilai a adalah', a)

a /= 2
print('nilai a/=2 adalah', a)

a = 3
print('nilai a adalah', a)

a **= 2 
print('nilai a**=2 adalah', a)

a = 35
print('nilai a adalah', a)

a %= 32
print('nilai a%=2 adalah', a)

a = 35
print('nilai a adalah', a)

a //= 32
print('nilai a//=2 adalah', a)

#TUGAS UNTUK MELANJUTKAN OPERATOR SELANJUTNYA
#SELANJUTNYA LINE 25-LINE 59

print('=============TUGAS=========')
#OR
b = True
print('Nilai b =', b)
b |= False
print('Nilai b|= False akan menjadi', b)
b = False
print('Nilai b =', b)
b |=False
print('Nilai b|= False akan menjadi', b)

#AND
b = True
print('Nilai b =', b)
b &= False
print('Nilai b&= False akan menjadi', b)
b = False
print('Nilai b =', b)
b &=False
print('Nilai b&= False akan menjadi', b)

#XOR
b = True
print('Nilai b =', b)
b ^= False
print('Nilai b^= False akan menjadi', b)
b = False
print('Nilai b =', b)
b ^=False
print('Nilai b^= False akan menjadi', b)

#SHIFTING
c = 0b0100
print('Nilai c =', format(c, '04b'))
c >>= 1
print('Nilai c >>=1 akan menjadi', format(c, '04b'))
c = 0b0100
c <<=1
print('Nilai c <<=1 akan menjadi', format(c, '04b'))


#  OPERATOR PERBADINGAN
print('======OPERATOR PERBANDINGAN======') 
a = 9 
b = 13
print('\n----------Besar dari  26')
hasil = a > 26
print(a, '> 26 adalah', hasil)
hasil = b > 26
print(b, '> 26 adalah', hasil)

print('\n----------kecil dari  26')
hasil = a < 26
print(a, '< 26 adalah', hasil)
hasil = b < 26
print(b, '< 26 adalah', hasil)

print('\n----------Besar atau sama dari 26')
hasil = a >= 26
print(a, ">= 26 adalah", hasil)
hasil = b >= 26
print(b, ">= 26 adalah", hasil)

print('\n----------Kecil atau sama dari 26')
hasil = a <= 26
print(a, "<= 26 adalah", hasil)
hasil = b <= 26
print(b, "<= 26 adalah", hasil)

print('\n----------Sama atau dari 26')
hasil = a == 26
print(a, "== 26 adalah", hasil)
print(b, "== 26 adalah", hasil)
hasil = b == 26

print('\n----------Tidak sama dari 26')
hasil = a != 26
print(a, "!= 26 adalah", hasil)
hasil = b != 26
print(b, "!= 26 adalah", hasil)

#OPERATOR LOGIKA
print("==========OPERATOR LOGIKA==========")
a = True
b = False
print('\n===========AND================')

hasil = a and a
print(a, 'and', a, 'hasilnya = ', hasil)

hasil = a and b
print(a, 'and', b, 'hasilnya = ', hasil)

hasil = b and a
print(b, 'and', a, 'hasilnya = ', hasil)

hasil = b and b
print(b, 'and', b, 'hasilnya = ', hasil)

print('\n==========OR================')
hasil = a or a
print(a, 'OR', a, 'hasilnya = ', hasil)

hasil = a or b
print(a, 'OR', b, 'hasilnya = ', hasil)

hasil = b or a
print(b, 'OR', a, 'hasilnya = ', hasil)

hasil = b or b
print(b, 'OR', b, 'hasilnya = ', hasil)

print('\n===========XOR================')

hasil = a ^ a
print(a, 'XOR', a, 'hasilnya = ', hasil)

hasil = a ^ b
print(a, 'XOR', b, 'hasilnya = ', hasil)

hasil = b ^ a
print(b, 'XOR', a, 'hasilnya = ', hasil)

hasil = b ^ b
print(b, 'XOR', b, 'hasilnya = ', hasil)

print('\n===========NOT================')

hasil =  not a
print('NOT', a, 'hasilnya = ', hasil)

hasil = not b
print('NOT', b, 'hasilnya = ', hasil)

# OPERATOR MEMBERSHIP
print("===========OPERATOR MEMBERSHIP============")

print('\n===========IN================')
nama = 'Fadhil Aditya'
test = 'dhil'
cek = test in nama
print(test, 'terdapat di', nama, 'adalah', cek )

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1, 'terdapat di', nama, 'adalah', cek)
cek = test2 in nama
print(test2, 'terdapat di', nama, 'adalah', cek)
cek = test3 in nama
print(test3, 'terdapat di', nama, 'adalah', cek)
cek = test4 in nama
print(test4, 'terdapat di', nama, 'adalah', cek)
cek = test5 in nama
print(test5, 'terdapat di', nama, 'adalah', cek)

print('\n==========NOT IN================')
#tugas lanjutkan untuk NOT IN dengan cara yang sama
cek = test1 not in nama
print(test1, 'tidak terdapat di', nama, 'adalah', cek)
cek = test2 not in nama
print(test2, 'tidak terdapat di', nama, 'adalah', cek)
cek = test3 not in nama
print(test3, 'tidak terdapat di', nama, 'adalah', cek)
cek = test4 not in nama
print(test4, 'tidak terdapat di', nama, 'adalah', cek)
cek = test5 not in nama
print(test5, 'tidak terdapat di', nama, 'adalah', cek)