string = "UNIVERSITAS GUNADARMA"
print('\n'.join(string[:i] for i in range(len(string)+1)))

# \n berarti newline
# \n.join(string[:i]) si \n masuk ke output si string
# berarti tiap print huruf sesuai banyak looping akan diberi
# baris baru
# len(string)+1 artinya tiap print huruf menambahkan 1 huruf didepannya sampai habis