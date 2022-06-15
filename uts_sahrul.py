print("Selamat Datang di ATM saya")
print("pilih option :")
print("1. Check Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Uang Saya")
option=int(input("silahkan pilih option :"))
if option==1:
    print("Uang Kamu Berjumlah Rp.500000")
elif option==2:
    print("Uang Kamu Berjumlah Rp.500000, Mau ambil berapa?")
    print("1. Rp.300.000")
    print("2. Rp.100.000")
    Uang_Kamu=500000
    option2=int(input("option :"))
    if option2==1:
        hasil=Uang_Kamu-300000
        print("Uang Kamu Sekarang Berjumlah :",hasil)
    elif option2==2:
        hasil2=Uang_Kamu-100000
        print("Uang Kamu Sekarang Berjumlah :",hasil2)
    else:
        print("Keyword Anda Salah")
elif option==3:
    uang_kamu=500000
    print("Uang berjumlah Rp.500.000, Mau Nabung Berapa?")
    option3=int(input("Masukkan Jumlah Uang :"))
    hasil3=uang_kamu+option3
    print("Jumlah Uang Kamu Sekarang Adalah",hasil3)
else:
    print("Keyword Anda Salah, Mohon Coba Lagi")