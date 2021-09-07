try:
    from selenium import webdriver
    #from selenium.webdriver.common.keys import Keys
    from time import sleep
    import re
    import random
    import os
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import openpyxl

    def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

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

    def wait(text:str):
        while True:
            source = str(browser.page_source)
            if source.find(text) < 0:
                sleep(2)
            else:
                break

    print('{:=^51}'.format('Programmed by Trần Thanh Hùng'))
    print('{:=^51}'.format('Contact for work: fb.com/darrenhtth'))
    print('{:=^51}'.format('Thanks for using'))

    set_time_min = int(input('Thời gian nhỏ nhất (phút): '))
    set_time_max = int(input('Thời gian lớn nhất (phút): '))
    id_sheet     = int(input('STT Sheet DNT2: ')) - 1
    '''
    i = 1
    getAccount = xlsdata.get_value_excel('data.xlsx', 'Wait', 'A'+str(i)).split('|')
    mailUser = getAccount[0] + '@yahoo.com'
    mailPass = getAccount[1]
    '''
    ### Get data bang
    print("Getting Data From Google Sheets...")
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    sleep(2)
    with open(r'C:\Users\Darren\path.txt', mode='w') as path:
        path.write(os.getcwd()+'\TestKhang-a7f8e46b006b.json')

    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd()+'\TestKhang-a7f8e46b006b.json', scope)
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

    with open('accbang.txt', mode='w+', encoding='utf-8') as file:
        for i in range(1,len(list_of_status)):
            if list_of_status[i] in ['Bang', 'bang', 'Băng', 'băng']:
                list_acc_bang.append(list_acc[i])
                list_pwd_bang.append(list_pwd[i])
                file.write(list_acc[i]+'\n'+list_pwd[i]+'\n')
    num_lines = sum(1 for line in open('accbang.txt'))
    if num_lines == 0:
        raise ImportError('Get WorkSheet DNT2: Failed!')
        sleep(3)
    else:
        print("Get WorkSheet DNT2: Successfully!")

    with open('accbang.txt', mode='r', encoding='utf-8') as file:
        for i in range(1,num_lines,2):
            mailUser = file.readline()
            mailPass = file.readline()
            detail_title    = get_value_excel(os.getcwd()+'\data.xlsx', 'Khang', 'B' + str(random.randint(2,11)))
            detail_deltails = get_value_excel(os.getcwd()+'\data.xlsx', 'Khang', 'F' + str(random.randint(1,1000)))
            detail_platform = 'Facebook'
            detail_link     = 'https://www.facebook.com/tiendung.bui.90'

            browser = webdriver.Chrome(os.getcwd()+'\chromedriver.exe')
            browser.get('https://ads.tiktok.com/i18n/login')
            browser.maximize_window()
            browser.find_element_by_id('TikTok_Ads_SSO_Login_Email_Input').send_keys(mailUser)
            sleep(0.431)
            browser.find_element_by_id('TikTok_Ads_SSO_Login_Pwd_Input').send_keys(mailPass)
            sleep(0.431)
            browser.find_element_by_id('TikTok_Ads_SSO_Login_Btn').click()

            #source = browser.page_source
            ###Get background image
            #captcha_background = re.search(r'<img draggable="false" src="(.*?)" alt="" class="', source).group(1)
            #browser.execute_script("window.open('about:blank', 'tab2');")
            # #browser.get(captcha_background)
            '''
            with open('C:\\Users\Darren\Desktop\Python\\background.png', 'wb') as file:
                file.write(browser.find_element_by_xpath(r'/html/body/div[1]/section/div[1]/section/div/div/section/div[4]/div/div[2]/section/div[5]/div/div/div[2]/img[1]').screenshot_as_png)
            with open('C:\\Users\Darren\Desktop\Python\piece.png', 'wb') as file:
                file.write(browser.find_element_by_xpath(r'/html/body/div[1]/section/div[1]/section/div/div/section/div[4]/div/div[2]/section/div[5]/div/div/div[2]/img[2]').screenshot_as_png)
            print('Downloaded!')
            sleep(3)
            ### Get distance
            sol           = PuzleSolver("C:\\Users\Darren\Desktop\Python\piece.png", "C:\\Users\Darren\Desktop\Python\\background.png")
            os.startfile("C:\\Users\Darren\Desktop\Python\sobel.png")
            captcha_distance = sol.get_position()
            print(captcha_distance)
            '''

            wait('vi-button vi-byted-button btn-small vi-button--primary vi-button--small')

            ###Next page: Click Account Info
            browser.find_element_by_xpath('/html/body/header/div/div[2]/div/div[4]/div/div/div/div')\
                .click()
            browser.find_element_by_xpath('/html/body/header/div/div[2]/div/div[4]/div/div[2]/div/ul[1]/li[2]/a')\
                .click()
            try:
                alert = browser.switch_to.alert
                alert.accept()
            except:
                print('')
            wait('Company Phone Number')
            sleep(random.randint(5,10))
            source    = browser.page_source
            com_phone = re.search(r'Company Phone Number</label><div class="vi-form-item__content" style="margin-left: 150px;"><span>(.*?)</span>', source).group(1)
            com_ID    = re.search(r'Business Verification ID</label><div class="vi-form-item__content" style="margin-left: 150px;"><span>(.*?)</span>', source).group(1)
            with open('id.txt', mode="w+") as id:
                id.write(com_ID)
            browser.find_element_by_xpath('/html/body/div[1]/section/div[4]').click()

            allTabs = browser.window_handles
            browser.switch_to.window(allTabs[1])
            sleep(random.uniform(1,3))

            wait('https://lf16-adcdn-sg.ibytedtos.com/obj/ad-platform-feedas-i18n-sg/548711a355494b43c8265eefa3d45f0a.png')
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div[9]').click()
            wait('Frozen Credit Appeals')
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/ul/li/ul/li/ul/div[2]/li/div').click()
            wait('  Submit ')
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div/div/div[2]/input').send_keys(detail_title)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/textarea').send_keys(detail_deltails)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div[2]/input').send_keys(detail_platform)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/input').send_keys(detail_link)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[8]/div/div/div[2]/input').send_keys(com_phone)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[9]/div/div/div[2]/input').send_keys(mailUser)

            ### Upload file
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[5]/div/div/div[2]/div[1]/div/div[1]/div').click()
            sleep(1)
            os.startfile(os.getcwd()+'\choosefilekhang1.exe')
            sleep(10)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[5]/div/div/div[2]/div[1]/div[2]/div[1]/div').click()
            sleep(1)
            os.startfile(os.getcwd()+'\choosefile.exe')
            sleep(10)
            browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[10]/div/button').click()
            wait('Are you sure you want to submit?')
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div/button[2]').click()
            #'<img draggable="false" src="https://p16-security-sg.ibyteimg.com/img/security-captcha-oversea-singapore/slide_b1f9e107a2741c09ae57a21e9e27cecdc856e6f0_1_1.jpg~tplv-obj.image" alt="" class="sc-gZMcBi YkDbM sc-ifAKCX hCcViW">'
            #'<img class="captcha_verify_img_slide react-draggable sc-gqjmRU irZaUl" alt="" src="https://p16-security-sg.ibyteimg.com/img/security-captcha-oversea-singapore/slide_b1f9e107a2741c09ae57a21e9e27cecdc856e6f0_2_1.png~tplv-obj.image" style="touch-action: none; left: 0px; top: 80.0725px; transform: translate(0px, 0px);">'
            sleep(5)
            browser.close()
            print('Kháng xong tài khoản:', mailUser)
            os.startfile(os.getcwd()+'\Faker.exe')
            time_sleep = random.randint(60*set_time_min, 60*set_time_max)
            for j in range(time_sleep, 0, -10):
                print(str(j)+'s', end='...' )
                sleep(10)
except Exception as bug:
    print(bug)
input()