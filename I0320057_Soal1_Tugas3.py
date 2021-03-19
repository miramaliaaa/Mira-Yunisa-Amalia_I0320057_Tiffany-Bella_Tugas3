NamaTeman = ['Halidya', 'Rara', 'Nadya', 'Hasna', 'Nana', 'Alam', 'Ojat', 'Ilham', 'Rapli', 'Waskita']
print("Nama Teman : ", NamaTeman)
print()
# Tampilkanlah isi list indeks nomor 4,6,7.

print("Nama Teman ke 4 : ", NamaTeman[4])
print("Nama Teman ke 6 : ", NamaTeman[6])
print("Nama Teman ke 7 : ", NamaTeman[7])
print()

# Gantilah nama teman mu yang berada di list 3,5,9

NamaTeman[3] = 'Sekar'
NamaTeman[5] = 'Vika'
NamaTeman[9] = 'Memed'
print()

print("Sebelum diubah : ", NamaTeman)
print("Nama Teman ke 3 diganti : ", NamaTeman[3])
print("Nama Teman ke 5 diganti : ", NamaTeman[5])
print("Nama Teman ke 9 diganti : ", NamaTeman[9])
print("Setelah diubah : ", NamaTeman)
print()

# Tambahkanlah 2 nama teman mu

NamaTeman.append('Alvin')
NamaTeman.append('Alica')
print("Nama Teman setelah ditambah : ", NamaTeman)
print()

# Tampilkan semua teman kamu dengan perulangan
print("Teman-temanku : ")
for nama in NamaTeman:
    print( nama)
print()

#Tampilkan panjang list

print("Temanku ada", len(NamaTeman))