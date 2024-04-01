jumlah_barang = int(input(' Masukan jumlah barang :'))
harga_satuan = int(input(' Masukan harga satuan barang : '))
total_harga = jumlah_barang * harga_satuan
print(' Total harga belanjaan anda adalah : ', total_harga)
uang_dibayarkan = int(input(' Masukan jumlah uang yang dibayarkan : '))
kembalian = uang_dibayarkan - total_harga

print(10*'=', 'Struk Belanja',10*'=')
print("Total Harga: Rp", total_harga)
print("Uang Dibayarkan: Rp", uang_dibayarkan)
print("Uang Kembalian : Rp", kembalian)
print("Terimakasih atas pembelian Anda!")