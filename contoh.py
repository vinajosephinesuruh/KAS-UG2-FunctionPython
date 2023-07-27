# def luas_persegi(sisi):
#     luas = sisi*sisi
#     return luas

# def keliling_persegi(sisi):
#     keliling = sisi*4
#     return keliling

# print("====KALKULATOR PERSEGI====")
# sisi = int(input("sisi persegi ="))
# print("luas persegi adalah",luas_persegi(sisi), "cm")
# print("keliling persegi adalah ",keliling_persegi(sisi),"cm")

# def celsius_to_reamur(suhu):
#     reamur = 4/5*suhu
#     return reamur

# def celsius_farenheit(suhu):
#     ferenheit = (9/5)*suhu+32
#     return ferenheit

# def celsius_kelvin(suhu):
#     kelvin = suhu + 273
#     return kelvin
# pilihan = input("ini mengkonversi suhu ke apa?")
# if pilihan == "kelvin":
#   suhu = int(input("suhu dalam celsius ="))
# elif pilihan == "ferenheit":
#     suhu = int(input(ferenheit))

# print("hasil konversi celsius to kelvin",celsius_kelvin(suhu),"kelvin")
# print(celsius_farenheit(suhu))


# # # suhu = int(input("suhu dalam celsius ="))
# # print("hasil konversi celsius to reamur",celsius_to_reamur(suhu),"reamur")
# # print(celsius_farenheit(suhu))
# print(celsius_kelvin(suhu))



print("==========Kalkulator cerdas==========")

def tabung(jari_jari, tinggi):
    Volume_tabung = jari_jari**2*tinggi
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

pilihan = int(input("masukan pilihan 1,2,3"))
if pilihan == "1":
    jari_jari = int(input("masukan jumlah sisi :"))
    tinggi = int(input("masukan jumlah tinggi"))
    print(tabung(jari_jari, tinggi))
elif pilihan == "2" : 
    sisi= int(input("masukan jumlah sisi:"))
    print(kubus(sisi))
elif pilihan == "3":
    panjang = int(input("masukan jumlah panjang :"))
    lebar = int(input("masukan lebar :"))
    tinggi = int(input("masukan tinggi"))
else:
    print("tidak ada pilihan")


