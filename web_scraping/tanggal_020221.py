# Proses pembuatan file : New Project, Git, Github, share project into github --> masuk ke repo ebe-dotcom

import bs4
import requests

url = 'http://jadwalsholat.pkpu.or.id/?id=83'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, features='html.parser')  # menampilkan seluruh isi web html

data = response.find_all('tr','table_dark')  # tipe data tr yang memiliki komponen tabel dark
print(data)  # Hasil print data diawali kurung siku dan diakhiri kurung siku, berarti data itu = data array/list

# so harus untuk mengolahnya ambil elemen pertama yaitu nomor 0
print(data[0])  # menghasilkan data tanpa kurung siku

#jadwal sholat ashar tanggal 2 februari 2021
sholat = {}
i = 0
data = data[0]

for d in data :
    if i == 1:
        sholat['shubuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1

print(sholat)
print('waktu sholat ashar tanggal 02 februari 2021',sholat['ashar'])

