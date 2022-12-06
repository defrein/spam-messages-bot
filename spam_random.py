import pyautogui
import time
import random

time.sleep(3)  # time for change your cursor position
n = 1000  # how much you want to spam
position = pyautogui.position()

when = ['Setahun yang lalu', 'Kemarin',
        'Tadi malam', 'Dahulu kala', 'Hari ini']
who = ['mahasiswa', 'bocil', 'bocah', 'anak', 'balita']
name = ['Widy', 'Akmal', 'Jamal', 'Vije', 'Ibnu']
residence = ['rumah orang tuanya', 'gedung DPR',
             'museum', 'bawah tanah', 'zaman batu']
went = ['isekai', 'kampus', 'pasar', 'rumah sakit', 'acara WIBU']
happened = ['menemukan teman sejatinya.', 'belajar mengendalikan cakra.',
            'menemukan sebuah kunci menuju Atlantis.', 'memutuskan untuk hidup bersama anime.', 'menerima misi untuk menyelamatkan dunia.']


for a in range(n):
    pyautogui.click(position.x, position.y)
    teks_random = (random.choice(when) + ', seorang ' + random.choice(who) + ' bernama ' + random.choice(name) + ' yang masih tinggal di ' + random.choice(
        residence) + ', pergi ke ' + random.choice(went) + ' kemudian dia ' + random.choice(happened))
    pesan = str(teks_random)
    pyautogui.typewrite(pesan)
    time.sleep(0.1)
    pyautogui.typewrite(["enter"])
    print(a)

print('sebanyak ' + str(n) + ' pesan berhasil dikirimkan.')
