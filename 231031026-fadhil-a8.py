chance = 3
latar_merah = "\033[101m"
latar_hijau = "\033[102m"
latar_cyan = "\033[106m"
putih = "\033[97m" 
berhenti = "\033[0m"
pw1 = 'fadhil123'
pw2 = '321fadhil'
pw3 = '12fadhil345'

while True:
    if chance != 0:
        try:
            inp = input('Silahkan masukkan password pertama: ')
            if inp == pw1:
                print(latar_cyan +'Berhasil' + berhenti)
                inp = input('Silahkan masukkan password kedua: ')
                if inp == pw2:
                    print(latar_cyan +'Berhasil' + berhenti)
                    inp = input('Silahkan masukkan password ketiga: ')
                    if inp == pw3:
                        print(latar_hijau + 'Anda berhasil login' + berhenti)
                        break
                    elif inp != pw3:
                        chance -= 1
                        print(latar_merah + 'Password salah.' + berhenti)
                        print(f'Kesempatan anda tersisa {chance} kali!')
                        continue
                    else:
                        print(latar_merah + 'Anda terblokir. Silahkan coba lain kali!' + berhenti)
                        break
                elif inp != pw2:
                    chance -= 1
                    print(latar_merah + 'Password salah.' + berhenti)
                    print(f'Kesempatan anda tersisa {chance} kali!')
                    continue
                else:
                    print(latar_merah + 'Anda terblokir. Silahkan coba lain kali!' + berhenti)
                    break
            elif inp != pw1:
                chance -= 1
                print(latar_merah + 'Password salah.' + berhenti)
                print(f'Kesempatan anda tersisa {chance} kali')
                continue

        except ValueError:
            print('Mohon masukkan format dengan benar!')
            chance -= 1
            print(f'Anda memiliki {chance} kesempatan tersisa!\n')
    else:
        print(latar_merah + 'Anda terblokir. Silahkan coba lain kali!' + berhenti)
        break