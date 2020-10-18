bConstant = 1
w = [[0, 0]]
b = [0]
xVal = [-1, -1, 1, 1]
yVal = [-1, 1, -1, 1]
target = [-1, 1, 1, 1]

print("Perubahan bobot:")
for n in range(4):
    print("Data Ke-", n+1)
    w1 = w[n][0] + (xVal[n] * target[n])
    w2 = w[n][1] + (yVal[n] * target[n])
    b_n = b[n] + (bConstant * target[n])
        
    print(f"w[1] = {w1}")
    print(f"w[2] = {w2}")
    print(f"b[{n+1}] = {b_n}\n")

    w.append([w1, w2])
    b.append(b_n)

# print(f"w = {w}")
# print(f"b = {b}")