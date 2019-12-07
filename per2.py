angka2 = int(input('Masukan ANGKA Kedua:'))
angka2 = int(input('Masukan ANGKA Kedua:'))
print('operator : 1.penjmlahan \n2. Pengurangan \n2
'3. Perkalian \n4. pembagian')
pilih=int(input('Pilih Operator :'))
if pilih == 1:
    tambah = angka1+angka2
    print('Hasilnya adalah ',tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print('Hasilnya adalah ',kurang)
elif pilih == 3:
    kali = angka1*angka2
    print('Hasilnya adalah ',kali)
elif pilih == 4:
    bagi = angka1/angka2
    print('Hasilnya adalah ',bagi))
else:
    print('Operator yang anda masukan tidak ada')
