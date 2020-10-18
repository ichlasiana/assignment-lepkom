batas = int(input("Masukkan Batas : "))
str_batas = ''.join([str(i+1) for i in range(batas)])

down = '\n'.join(str_batas[:i] for i in range(batas, 0, -1))
up = '\n'.join(str_batas[:i] for i in range(2, batas+1))
print(f"{down}\n{up}")