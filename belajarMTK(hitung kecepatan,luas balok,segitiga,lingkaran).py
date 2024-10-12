print('RUMUS DARI BANGUN RUANG')

def rumus_kecepatan():
    print('Rumus Kecepatan siap!')
    jarak = float(input('Masukkan jarak :'))
    waktu = float(input('Masukkan Waktu :'))
    Kecepatan = (jarak * waktu)
    print ('\nkecepatan=', Kecepatan)

def luas_segitiga():
    print('Rumus Luas segitiga siap!')
    Alas = float(input('Masukkan Alas :'))
    Tinggi = float(input('Masukkan Tinggi :'))
    Luas = (0.5 * Alas * Tinggi)
    print ('\nLuas=', Luas)

def luas_balok():
    print('Rumus Luas balok siap!')
    panjang = float(input('Masukkan panjang :'))
    Lebar = float(input('Masukkan Lebar :'))
    Tinggi = float(input('Masukkan Tinggi :'))
    Luas = (2*panjang*Lebar ) + (2*panjang*Tinggi) + (2*Lebar*Tinggi)
    print ('\nkecepatan=', Luas)

def Luas_bulat():
    print('Rumus Luas Bulat siap!')
    r = float(input('Masukkan Jari jari :'))
    Luas = (4 * 3.14 ** r)
    print ('\nLuas=', Luas)
    

while True:
    User_input = input('Pilih Rumus yang akan dipakai: \n\n1.Mencari Kecepatan \n2.Luas segitiga \n3.Luas Balok \n4.Luas Lingkaran\nTekan 0 untuk berhenti\n\nPilih nomor berapa?')
    if (User_input == "1"):
        rumus_kecepatan()
    elif(User_input == '2'):
        luas_segitiga()
    elif(User_input == "3"):
        luas_balok()
    elif(User_input == "4"):
        Luas_bulat()
    else:
        break