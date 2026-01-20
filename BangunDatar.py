def luasPersegi(sisi):
    return sisi * sisi

def kelilingPersegi(sisi):
    return 4 * sisi


def luasPersegiPanjang(panjang, lebar):
    return panjang * lebar

def kelilingPersegiPanjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luasSegitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def kelilingSegitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luasLingkaran(jariJari):
    return 3.14 * jariJari * jariJari

def kelilingLingkaran(jariJari):
    return 2 * 3.14 * jariJari

def luasJajarGenjang(alas, tinggi):
    return alas * tinggi
def kelilingJajarGenjang(sisiMiring, sisiSejajar):
    return 2 * (sisiMiring + sisiSejajar)

print("Program Bangun Datar")

nama = input("Masukan Nama Anda:")

print(nama,", Selamat Datang di Program Bangun Datar")

print("Pilih Bangun Datar:")
daftar_bangun_datar = ["1. Persegi", "2. Persegi Panjang", "3. Segitiga", "4. Lingkaran", "5. Jajar Genjang"]
i = 0

while i < len(daftar_bangun_datar):
    print(daftar_bangun_datar[i])
    i += 1

try:
    pilihan = int(input("Masukan Pilihan Anda (1-5): "))
except ValueError:
    print("Pilihan Tidak Valid")


while True:
    if pilihan == 1:
        try:
            sisi = int(input("Masukan Sisi Persegi: "))
        except ValueError:
            print("Pilihan Tidak Valid")    
        print("Luas Persegi adalah:", luasPersegi(sisi))
        print("Keliling Persegi adalah:", kelilingPersegi(sisi))
    elif pilihan == 2:
        try:
            panjang = int(input("Masukan Panjang Persegi Panjang: "))
            lebar = int(input("Masukan Lebar Persegi Panjang: "))
        except ValueError:
            print("Pilihan Tidak Valid")
        print("Luas Persegi Panjang adalah:", luasPersegiPanjang(panjang, lebar))
        print("Keliling Persegi Panjang adalah:", kelilingPersegiPanjang(panjang, lebar))
    elif pilihan == 3:
        try:
            alas = int(input("Masukan Alas Segitiga: "))
            tinggi = int(input("Masukan Tinggi Segitiga: "))
            sisi1 = int(input("Masukan Sisi 1 Segitiga: "))
            sisi2 = int(input("Masukan Sisi 2 Segitiga: "))
            sisi3 = int(input("Masukan Sisi 3 Segitiga: "))
        except ValueError:
            print("Pilihan Tidak Valid")
        print("Luas Segitiga adalah:", luasSegitiga(alas, tinggi))
        print("Keliling Segitiga adalah:", kelilingSegitiga(sisi1, sisi2, sisi3))
    elif pilihan == 4: 
        try:
            jariJari = int(input("Masukan Jari-Jari Lingkaran: "))
        except ValueError:
            print("Pilihan Tidak Valid")
        print("Luas Lingkaran adalah:", luasLingkaran(jariJari))
        print("Keliling Lingkaran adalah:", kelilingLingkaran(jariJari))
    elif pilihan == 5:
        try:
            alas = int(input("Masukan Alas Jajar Genjang: "))
            tinggi = int(input("Masukan Tinggi Jajar Genjang: "))
            sisiMiring = int(input("Masukan Sisi Miring Jajar Genjang: "))
            sisiSejajar = int(input("Masukan Sisi Sejajar Jajar Genjang: "))
        except ValueError:
            print("Pilihan Tidak Valid")
        print("Luas Jajar Genjang adalah:", luasJajarGenjang(alas, tinggi))
        print("Keliling Jajar Genjang adalah:", kelilingJajarGenjang(sisiMiring, sisiSejajar))

    else:
        print("Pilihan Tidak Tersedia")

    lagi = input("Apakah Anda Ingin Menghitung Lagi? (y/n): ")

    if(lagi == "y"):
        print("Silahkan Jalankan Program Ulang")
        continue
    else:
        print("Terima Kasih", nama)
        break

