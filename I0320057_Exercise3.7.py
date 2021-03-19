#Contoh cara menghapus pada Dictionary Python

dict = {'Name': 'Mira', 'Age': 18, 'Class': 'First'}

del dict['Name'] #hapus entri dengan key 'Name'
dict.clear()     #hapus semua entri di dict
del dict         #hapus dictionary yang sudah ada

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])