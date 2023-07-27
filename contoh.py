print("==========Kalkulator cerdas==========")

def tabung(jari_jari, tinggi):
    pi=22/7
    Volume_tabung = pi*jari_jari*tinggi
    return Volume_tabung

def kubus(sisi):
    Volume_kubus = sisi**3
    return Volume_kubus

def balok(panjang, lebar, tinggi):
    volume_balok =panjang*lebar*tinggi
    return volume_balok

print("pilihan bangun yang ingin di hitung")
print("1.Tabung")
print("2. Kubus")
print("3.Balok")

pilihan = int(input("masukan pilihan 1,2,3: "))
if pilihan == 1:
    jari_jari = int(input("masukan diameter :"))
    tinggi = int(input("masukan jumlah tinggi: "))
    print(tabung(jari_jari, tinggi))
elif pilihan == 2 : 
    sisi= int(input("masukan jumlah sisi:"))
    print(kubus(sisi))
elif pilihan == 3:
    panjang = int(input("masukan jumlah panjang :"))
    lebar = int(input("masukan lebar :"))
    tinggi = int(input("masukan tinggi :"))
    print(balok(panjang, lebar, tinggi))
else:
    print("tidak ada pilihan")


