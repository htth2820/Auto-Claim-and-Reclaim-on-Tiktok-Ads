import openpyxl

def get_value_excel(filename, sheetname, cellname):
    wb = openpyxl.load_workbook(filename)
    Sheet = wb[sheetname]
    wb.close()
    return Sheet[cellname].value

def update_value_excel(filename, sheetname, cellname, value):
    wb = openpyxl.load_workbook(filename)
    Sheet = wb[sheetname]
    Sheet[cellname].value = value
    wb.close()
    wb.save(filename)

def getIdProvince(province:str):
    arrPro = ['Gyeonggi-do','Incheon','Gwangju','Jeollabuk-do','Jeonnam-do',
              'Daegu','Daegu','Chungcheongbuk-do','Chungcheongnam-do','Gyeongsangbuk-do',
              'Gyeongsangnam-do','Gangwon-do','Jeju-do','Ulsan','Busan','Seoul','Sejong City']
    if province in arrPro:
        return arrPro.index(province) + 1
    else:
        raise ValueError('Province Not Found!')
