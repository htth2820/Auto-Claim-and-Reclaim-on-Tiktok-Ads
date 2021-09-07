from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import random
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openpyxl
import datetime

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

id_sheet     = int(input('STT Sheet DNT2: ')) - 1
print("Getting Data From Google Sheets...")
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
sleep(2)
with open(r'C:\Users\Darren\path.txt', mode='w') as path:
    path.write(resource_path('TestKhang-a7f8e46b006b.json'))

creds = ServiceAccountCredentials.from_json_keyfile_name(resource_path('TestKhang-a7f8e46b006b.json'), scope)
client = gspread.authorize(creds)
sheets = client.open("Lập tài khoản tiktok Hàn quốc - TIẾN - File TỔNG lên camp")

sheet_DNT2 = sheets.get_worksheet(id_sheet)
list_of_status = sheet_DNT2.col_values(25)
print('Number of Account:', len(list_of_status))
list_acc       = sheet_DNT2.col_values(20)
list_pwd       = sheet_DNT2.col_values(21)
print('Number of Password:',len(list_pwd))
if len(list_of_status)>len(list_pwd):
    for i in range(len(list_pwd)+1, len(list_of_status)+1):
        sheet_DNT2.update_cell(i, 21, 'None')
list_pwd       = sheet_DNT2.col_values(21)
list_acc_bang    = []
list_pwd_bang    = []
list_stt_bang    = []
count_bang       = 0
with open('accbang.txt', mode='w+', encoding='utf-8') as file:
    for i in range(1,len(list_of_status)):
        if list_of_status[i] in ['Bang', 'bang', 'Băng', 'băng']:
            count_bang += 1
            list_stt_bang.append(i)
            if str(list_acc[i]).find('|') < 0:
                list_acc_bang.append(list_acc[i])
                list_pwd_bang.append(list_pwd[i])
                file.write(list_acc[i]+'\n'+list_pwd[i]+'\n')
            else:
                info_acc = str(list_acc[i]).split('|')
                list_acc_bang.append(info_acc[0]+'@yahoo.com')
                list_pwd_bang.append(info_acc[1])
                file.write(info_acc[0]+'@yahoo.com'+'\n'+info_acc[1]+'\n')
num_lines = sum(1 for line in open('accbang.txt'))
if num_lines == 0:
    raise ImportError('Get WorkSheet DNT2: Failed!')
    sleep(3)
else:
    print("Get WorkSheet DNT2: Successfully!")
stt_bang = 0