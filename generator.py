import random
import sys
import pyperclip

soal_list = []
nama_list = []

with open('soal_list.txt', 'r') as file:
    _file = file.read()
    _soal = _file.split('\n')
    soal_list = _soal
    file.close()

with open('name_list.txt', 'r') as file:
    _file = file.read()
    _nama = _file.split('\n')
    nama_list = _nama

selected_soal = []

while len(selected_soal) < 35:
    _selected_soal = soal_list[random.randint(0, len(selected_soal))]
    if _selected_soal not in selected_soal:
        selected_soal.append(_selected_soal)

print(nama_list[0])
header = "Nama :  " + nama_list[0] + "\n*Tentukan IP Network, IP Awal, IP Akhir dan IP Broadcast dari IP Address dibawah ini!*\n\n"
soal = "\n".join(selected_soal)
tugas = header + soal

pyperclip.copy(tugas)

nama_list.remove(nama_list[0])

with open('name_list.txt', 'w') as file:
    file.write("\n".join(nama_list))