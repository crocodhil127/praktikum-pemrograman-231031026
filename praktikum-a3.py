nama = 'fadhil aditya'
nim = '231031026'
meet = 'praktikum 3'
prodi = 'sistem informasi A'
email = 'fadhiladitya551@gmail.com'
sp = 45
ttl = 'pembasean, 27 oktober 2005'
alamat = 'Kost Pondok Syafira'
asal = 'malili, luwu timur'
hobi = 'Mabar ML'
tinggi = '165'


print('-'*46)
print(f'{nama.upper().center(sp)}')
print(f'{nim.center(sp)}\n\n')
print(f'{meet.capitalize().rjust(sp)}')
print(f'{prodi.title().rjust(sp)}')
print(f'{email.rjust(sp)}')
print('-'*46)

print(f'\tHalo, nama saya {nama.title()} dengan NIM {nim} dari prodi {prodi.title()}, ini adalah file {meet.title()}. Terima kasih.\n')

print(f'''Biodata Saya,
Nama\t:{nama.title()}
Prodi\t:{prodi.title()}
NIM\t:{nim}
TTL\t:{ttl.title()}
Alamat\t:{alamat.title()}
Asal\t:{asal.title()}
Hobi\t:{hobi}
Tinggi\t:{tinggi}cm
      ''')


stat = 'Newton Frankel Issac'
up   = stat.upper()
print(up)
up = up.split() # up menjadi list n item
print(up)
print(up[-1][0],' '.join(up[0:-1])) #N SIR ISSAC
print('F SIR ISSAC NEWTON')

print(up[-1],up[0][0],up[1][0])
print('NEWTON S I')

print()

stat2 = '&sir$ @issac# *newton.'
up2   = stat2.upper()
print(up2)
up2   = up2.split() 
print(up2)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))
print('SIR ISSAC NEWTON')




