awal = int(input('Masukkan awal deret : '))
akhir = int(input('Masukkan akhir deret : '))
for i in range(awal,akhir):
    if i%3 != 0 or i%6 != 0:
        if i%2 == 1:
            print(i,end = ' ')
        else:
            continue
    else:
        continue