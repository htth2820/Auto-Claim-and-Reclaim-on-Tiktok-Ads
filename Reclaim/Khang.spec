# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/Khang.py'],
             pathex=['C:\\Users\\Darren\\Desktop\\Python\\Gomhang.vn\\Khang'],
             binaries=[],
             datas=[('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/aCountry.txt', '.'), ('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/choosefile.exe', '.'), ('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/choosefilekhang1.exe', '.'), ('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/chromedriver.exe', '.'), ('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/data.xlsx', '.'), ('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/Faker.exe', '.'), ('C:/Users/Darren/Desktop/Python/Gomhang.vn/Khang/TestKhang-a7f8e46b006b.json', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Khang',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\Darren\\Desktop\\Python\\Gomhang.vn\\Khang\\icon.ico')
