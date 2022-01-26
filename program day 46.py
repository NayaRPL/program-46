print("membuat struk pembayaran")
harga_sewa_kode_p=4000
harga_pelanggan_umum=5000
kode=input("masukkan kode:")
for i in kode:
    jam=int(input("banyak jam yang di sewa:"))
    uang=int(input("masukkan jumlah uang :"))
    
if kode == "p":
        if jam >=5 :
            total_harga_kotor=harga_sewa_kode_p*jam
            potongan_harga=(50/100*total_harga_kotor)
            total_pembayaran=total_harga_kotor-potongan_harga
            uang_kembali=uang-total_pembayaran
            print("total harga kotor:",total_harga_kotor)
            print("potongan_harga:",potongan_harga)
            print("total harga setelah mendapatkan diskon adalah:",total_pembayaran)
            print("jumlah uang yang tersisah dari pembayaran adalah:",uang_kembali)
        elif jam >=3:
            total_harga_kotor=harga_sewa_kode_p*jam
            potongan_harga=(30/100*total_harga_kotor)
            total_pembayaran=total_harga_kotor-potongan_harga
            uang_kembali=uang-total_pembayaran
            print("total harga kotor:",total_harga_kotor)
            print("potongan_harga",potongan_harga)
            print("total harga setelah mendapatkan diskon adalah:",total_pembayaran)
            print("jumlah uang yang tersisah dari pembayaran adalah:",uang_kembali)
elif kode == "u": 
        if jam >=5 :
            total_harga_kotor=harga_pelanggan_umum*jam
            potongan_harga=(50/100*total_harga_kotor)
            total_pembayaran=total_harga_kotor-potongan_harga
            uang_kembali=uang-total_pembayaran
            print("total harga kotor:",total_harga_kotor)
            print("potongan_harga:",potongan_harga)
            print("total harga setelah mendapatkan diskon adalah:",total_pembayaran)
            print("jumlah uang yang tersisah dari pembayaran adalah:",uang_kembali)
        elif jam >=3:
            total_harga_kotor=harga_pelanggan_umum*jam
            potongan_harga=(30/100*total_harga_kotor)
            total_pembayaran=total_harga_kotor-potongan_harga
            uang_kembali=uang-total_pembayaran
            print("total harga kotor:",total_harga_kotor)
            print("potongan_harga:",potongan_harga)
            print("total harga setelah mendapatkan diskon adalah:",total_pembayaran)
            print("jumlah uang yang tersisah dari pembayaran adalah:",uang_kembali)   
