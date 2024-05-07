def hitung():
    # Input bilangan pertama
    bilangan_pertama = float(input("Masukkan bilangan pertama: "))
    
    # Input bilangan kedua
    bilangan_kedua = float(input("Masukkan bilangan kedua: "))
    
    # Penjumlahan
    hasil_penjumlahan = bilangan_pertama + bilangan_kedua
    print("Hasil penjumlahan:", hasil_penjumlahan)
    
    # Pengurangan
    hasil_pengurangan = bilangan_pertama - bilangan_kedua
    print("Hasil pengurangan:", hasil_pengurangan)
    
    # Modus
    # Modus adalah bilangan yang paling sering muncul.
    # Dalam konteks ini, kita akan menemukan bilangan mana yang lebih sering muncul.
    if bilangan_pertama == bilangan_kedua:
        print("Modus: Tidak ada modus karena kedua bilangan sama.")
    else:
        if bilangan_pertama > bilangan_kedua:
            print("Modus:", bilangan_pertama)
        else:
            print("Modus:", bilangan_kedua)

# Memanggil fungsi hitung()
hitung()


