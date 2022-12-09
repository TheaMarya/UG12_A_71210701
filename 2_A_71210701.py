baris = input("masukkan nama : ")
kolom = 2 * len(baris) - 2
for noBaris in range(0, len(baris) - 1):
    for noKolom in range(0, kolom):
        print(end='')
    kolom -= 2
    for noKolom in range(0, noBaris + 1):
        print(f'{baris[noKolom]}', end='')
    print('')
kolom = -1

for noBaris in range(len(baris) - 1, -1, -1):
    for noKolom in range(kolom, -1, -1):
        print(end='')
    kolom += 2
    for noKolom in range(0, noBaris + 1):
        print(f'{baris[noKolom]}', end='')
    print('')