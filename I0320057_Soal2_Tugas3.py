#Nama, sosial media, lagu kesukaan, makanan favorit
Biodata = {'Nama': 'Mira',
           'Hobi' : ['Travelling',
                     'Olahraga',
                     'Mendengarkan musik'] ,
           'Sosial Media' : ['Ig = miramaliaaa',
                             'Line = mir.amalia',
                             'Facebook = Mira Amalia'],
           'Lagu Kesukaan' : ['Be Alright-Dean Lewis',
                              'Kukira Kau Rumah-Amigdala',
                              'September Song-JP Cooper'],
           'Makanan Favorit' : ['Sate',
                                'Ketoprak',
                                'Cake']}
print("Nama : ", Biodata['Nama'])
print("Hobi : ", Biodata['Hobi'])
print("Sosial Media : ", Biodata['Sosial Media'])
print("Lagu Kesukaan : ", Biodata['Lagu Kesukaan'])
print("Makanan Favorit : ", Biodata['Makanan Favorit'])

print()

for tujuan, maksud in Biodata.items():
      if type(maksud) == list:
          for i in range(len(maksud)):
              print("{} {} : {}".format(tujuan, i+1, maksud[i]))
      else:
          print("{} : {}".format(tujuan, maksud))

print()
#ubah salah satu dari hobi dan sosial media kalian, hapus lah 2 makanan favorit kalian, dan tambahkan lah 1 hoby kalian

Biodata['Hobi'][1] = 'Memasak'
Biodata['Sosial Media'][2] = 'Email = mirayunisaamalia@gmail.com'
del Biodata['Makanan Favorit'][:2]
Biodata['Hobi'].append('Menonton Film')

print('Setelah diubah : ')
print("Nama : ", Biodata['Nama'])
print("Hobi : ", Biodata['Hobi'])
print("Sosial Media : ", Biodata['Sosial Media'])
print("Lagu Kesukaan : ", Biodata['Lagu Kesukaan'])
print("Makanan Favorit : ", Biodata['Makanan Favorit'])

print()

for tujuan, maksud in Biodata.items():
      if type(maksud) == list:
          for i in range(len(maksud)):
              print("{} {} : {}".format(tujuan, i+1, maksud[i]))
      else:
          print("{} : {}".format(tujuan, maksud))