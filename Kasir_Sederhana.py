def kasir():
    # Daftar harga barang
    harga_barang = {
        "Pensil": 10000,
        "Buku": 15000,
        "Penghapus": 5000,
        "Bolpoint": 7000
    }

    print("========== BARANG ==========")
    for barang, harga in harga_barang.items():
        print(f"{barang} RP. {harga:,}")
    print("=============================")

    detail_belanja = []
    total_belanja = 0

    while True:
        barang = input('Masukkan nama barang: ').strip()
        
        # Cek apakah barang ada dalam daftar
        if barang not in harga_barang:
            print("Barang tidak ditemukan. Silakan coba lagi.")
            continue

        try:
            jumlah = int(input('Jumlah barang: '))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk jumlah.")
            continue

        total = jumlah * harga_barang[barang]
        total_belanja += total
        detail_belanja.append({"barang": barang, "total": total})

        respon = input('Apakah anda ingin membeli lagi (Y/N): ').strip().upper()
        if respon != "Y":
            break

    # Menampilkan nota
    print("\nNOTA")
    print("Detail belanja anda:")
    for detail in detail_belanja:
        print(f"-- {detail['barang']} \t {detail['total']:,}")
    print(f"Total belanja adalah {total_belanja:,}")

# Memanggil fungsi kasir
kasir()