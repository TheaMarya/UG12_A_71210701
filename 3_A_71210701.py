pembatas = int(input('Masukkan Pembatas : '))
dilarang = int(input('Masukkan Angka yang dilarang : '))
for i in range(pembatas):
    if i != dilarang:
        print(i,end =' ')
    else:
        continue