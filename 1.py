abjad = [chr(alph) for alph in range(65, 91)]
abjad_terbalik = abjad[::-1]
for i in range(0, 26, 2):
    print(f"{abjad[i]} {abjad[i+1]} | {abjad_terbalik[i]} {abjad_terbalik[i+1]}")

# gunain chr() biar baca abjad dari ASCII
# cek dari nomor ASCII keberapa disini https://www.rapidtables.com/code/text/ascii-table.html
# [:: -1] membalik list seperti pada modul CC
# pakai range(0, 26, 2) untuk outputnya 2, contoh :
# for i in range(0, 26, 2):
#   print(i)
# maka outputnya : [0. 2, 4, 6, 8, 10, 12, 24, 16, 18, 20, 22, 24]
# 26 gaikut, karena dimulai dari 0. dan sebagai batas looping, 
# jadi kalau udah 26, dia gabakal print 26. melainkan angka terakhir
# untuk statement print, gunakan f-string. {} merupakan pengambilan nilai dari abjad dan abjad_terbalik