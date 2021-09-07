import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\Darren\Desktop\Python\Gomhang.vn\Khang\TestKhang-a7f8e46b006b.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheets = client.open("Lập tài khoản tiktok Hàn quốc - TIẾN - File TỔNG lên camp")
sheet_DNT2 = sheets.get_worksheet(18)

# Extract and print all of the values
list_of_status = sheet_DNT2.col_values(25)
list_acc       = sheet_DNT2.col_values(20)
list_pwd       = sheet_DNT2.col_values(21)
list_acc_bang    = []
list_pwd_bang    = []
with open('accbang.txt', mode='w+', encoding='utf-8') as file:
    for i in range(1,len(list_of_status)):
        if list_of_status[i] in ['Bang', 'bang', 'Băng', 'băng']:
            list_acc_bang.append(list_acc[i])
            list_pwd_bang.append(list_pwd[i])
            file.write(list_acc[i]+'\n'+list_pwd[i]+'\n')

#with open('test.txt', mode='w+', encoding='utf-8') as file:
 #   for i in range(0,len(list_of_hashes)):
  #      for j in range(0,len(list_of_hashes[i])):
   #         file.write(list_of_hashes[i][j]+'\t')
#print(sheet_DNT2.col_count)
# Get values in a single row/col/cell
#data = sheet1.col_values(1)
#print(data)
# Update cell
#sheet2 = sheets.get_worksheet(1)
#sheet2.update_cell(1, 1, 'Trần Thanh Hùng')

### Create a Separate Sheet
# add a sheet with 20 rows and 2 columns
#sheets.add_worksheet(rows=20,cols=2,title='Test API')
# get the instance of the second sheet
#sheet_runs = sheets.get_worksheet(1)