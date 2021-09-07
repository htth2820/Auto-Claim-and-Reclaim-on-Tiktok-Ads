from cx_Freeze import setup, Executable


base = None

executables = [Executable("Khang.py", base=base)]

packages = ["socks","openpyxl","oauth2client.service_account","gspread","os",'random','re','selenium','selenium.webdriver.common.keys',"time"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<any name>",
    options = options,
    version = "1.0",
    description = '1.0',
    executables = executables
)