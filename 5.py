uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))

nilai_kehadiran = 1
if not all([uts, uas]):
    nilai_kehadiran = 0

total = (uts*.7 + uas*.3) * nilai_kehadiran
print("Total Nilai = ", round(total, 3))

ipk = {85:'A', 75:'B', 45:'C', 5:'D', 0:'E'}
for nilai in ipk.keys():
    if total >= nilai:
        print("IPK : ", ipk[nilai])
        break