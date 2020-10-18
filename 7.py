import math

print("Masukkan array X,Y,C1,C2 (tiap element dipisahkan dengan spasi)")
X = list(map(int, input("X = ").split()))   # 7 element
Y = list(map(int, input("Y = ").split()))   # 7 element
C1 = list(map(int, input("C1 = ").split()))
C2 = list(map(int, input("C2 = ").split()))

for i in range(4):
    M1 = math.sqrt((X[i] - C1[0])**2 + (Y[i] - C1[1])**2)
    M2 = math.sqrt((X[i] - C2[0])**2 + (Y[i] - C2[1])**2)
    print(f"({X[i]}, {Y[i]}) Jarak dari m1 = {'%g'%round(M1, 2)}")
    print(f"({X[i]}, {Y[i]}) Jarak dari m1 = {'%g'%round(M2, 2)}")