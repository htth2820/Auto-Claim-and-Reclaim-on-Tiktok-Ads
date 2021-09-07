import xlsdata
import openpyxl
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import threading
from multiprocessing import Pool
from random import randint
import os
############print(random.uniform(1.2, 3.2))
def wait(text:str):
    while True:
        source = str(browser.page_source)
        if source.find(text) < 0:
            sleep(3)
        else:
            break

print('{:=^51}'.format('Programmed by Trần Thanh Hùng'))
print('{:=^51}'.format('Contact for work: fb.com/darrenhtth'))
print('{:=^51}'.format('Thanks for using'))

###Get data
for i in range(2,10):
    print("Getting Data From Excel...")
    getAccount = xlsdata.get_value_excel('data.xlsx', 'VN', 'A'+str(i)).split('|')
    mailUser = getAccount[0]
    mailPass = getAccount[1]

    getInfor = xlsdata.get_value_excel('data.xlsx', 'VN', 'B'+str(i)).split('\n')
    com_name = getInfor[0]
    com_web      = getInfor[1]
    com_boss     = getInfor[3]
    com_street   = getInfor[2]
    com_phone    = getInfor[7]
    com_ID       = getInfor[5]
    com_name_Eng = getInfor[6]
    split_addr   = getInfor[2].split(', ')
    com_province     = split_addr[0]
    com_ID_province  = xlsdata.getIdProvince(com_province)
    com_district     = split_addr[1]
    com_zipcode      = split_addr[2]

    com_ID       = ''.join(getInfor[6].split('-'))
    print("Get Data Successfully!")

    with open('id.txt', mode="w+") as file:
        file.write(com_ID)
###Main
    com_country  = input('Input country name: ')
    browser = webdriver.Chrome(executable_path='chromedriver.exe')
    browser.get('https://ads.tiktok.com/i18n/signup')
    browser.maximize_window()

    try:
        accept = browser.find_element_by_xpath('/html/body/div[1]/section/div[3]/div/button').click()
    except:
        print('')
    country = browser.find_element_by_xpath(
              '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[2]/div[2]/form/div[1]/div/div[1]/div[1]/input')
    country.click()
    sleep(1.2)
    country.send_keys(com_country)
    sleep(1)
    country.send_keys(Keys.ARROW_DOWN)
    country.send_keys(Keys.ENTER)

    #country = browser.find_element_by_xpath(
    #          '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[2]/div[2]/form/div[1]/div/div[1]/div[2]/div/div[1]/ul/li[116]').click()
    next = browser.find_element_by_xpath(
              '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[2]/div[2]/form/div[3]/div/div/button[2]').click()
    #next = browser.find_element_by_xpath(
     #         '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[2]/div/div/div/div[4]/button/span').click()
    email = browser.find_element_by_xpath(
              '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[1]/div[2]/div/div/div/input')\
        .send_keys(mailUser+ '@yahoo.com')
    sleep(0.1231)
    pwd = browser.find_element_by_xpath(
              '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[2]/div/div/div/input')\
        .send_keys(mailPass)
    sleep(0.3231)
    repwd = browser.find_element_by_xpath(
              '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[3]/div/div/div/input')\
        .send_keys(mailPass)
    sleep(0.61231)
    send_code = browser.find_element_by_xpath(
              '/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[4]/div/div/div[2]').click()
    sleep(4.151)

###Tab Yahoo
    browser.execute_script("window.open('about:blank', 'tab2');")
    browser.switch_to.window("tab2")
    #https://login.yahoo.com/?.src=ym&.lang=en-GB&.intl=gb&.done=https%3A%2F%2Fmail.yahoo.com%2Fd
    browser.get('https://login.yahoo.com/')

    browser.find_element_by_id('login-username').send_keys(mailUser)
    browser.find_element_by_id('login-signin').click()
    sleep(randint(3,5))
    wait('password')

    browser.find_element_by_id('login-passwd').send_keys(mailPass)
    sleep(randint(1,2))
    browser.find_element_by_id('login-signin').click()
    browser.get('https://mail.yahoo.com/')
    sleep(randint(4,6))
    try:
        browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[7]/div/div/div/div[3]/div[5]/button').click()
    except:
        print('')
#####Gửi mail thất bại come back gửi lại
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/ul/li[3]/a').click()
    act_code = re.search(r'Here is your verification code: (.*?) It is valid within 10 minutes.',browser.page_source).group(1)
    print('Activation Code =', act_code)

###Tab Tiktok
    allTabs = browser.window_handles
    browser.switch_to.window(allTabs[0])
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[4]/div/div/div[1]/input')\
        .send_keys(act_code)
    sleep(0.5231)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[5]/div[1]/div')\
        .click()
    sleep(0.5231)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/div[3]/section/div[2]/main/form/div[7]/div/button[2]')\
        .click()
    wait('Each of the Customer and TikTok')
    sleep(2.513)

###Next page: Input: Name + PhoneNumber

#   /html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/section/form/div[1]/div[1]/div[2]/div/div[1]
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/section/form/div[1]/div[1]/div[2]/div/div[1]/input')\
        .send_keys(mailUser)
    sleep(0.8231)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/section/form/div[1]/div[2]/div[2]/div/div[1]/input')\
        .send_keys(com_phone)
    sleep(0.5)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight/4)") #Scroll down
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/section/form/div[2]/div[1]/div[2]/label/span/span')\
        .click()
    sleep(0.31)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/section/div/div/section/div[5]/div/section/form/div[3]/div/button')\
        .click()
    wait('Continue')

###Next page: Click Account Info
    browser.find_element_by_xpath('/html/body/header/div/div[2]/div/div[4]/div/div/div/div')\
        .click()
    browser.find_element_by_xpath('/html/body/header/div/div[2]/div/div[4]/div/div[2]/div/ul[1]/li[2]/a')\
        .click()
    alert = browser.switch_to.alert
    alert.accept()
    sleep(randint(5,10))
####
    wait('vi-icon-plus')

###Next page: Fill in Informations
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[2]/div/div[1]/input')\
            .send_keys(com_name_Kor)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[3]/div/div[1]/textarea')\
            .send_keys(com_web)

###Select Industry
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight/4)") #Scroll down
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[4]/div[1]/div/div/div[1]/span/span/i')\
        .click() #click to drop list
    sleep(randint(1,3)) #wait drop list
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[4]/div[1]/div/div/div[2]/div/div[1]/ul/li['+str(randint(1,29))+']/span')\
        .click() #click random Industry
    sleep(0.61)

###Select Sub-Industry
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[4]/div[2]/div/div/div[1]/span/span/i').click()
    sleep(randint(1,3))
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[4]/div[2]/div/div/div[2]/div/div[1]/ul/li['+str(randint(1,3))+']/span').click()

###Fill Street
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[5]/div/div[1]/input')\
            .send_keys(com_street)
    sleep(1.1231)

###Select Province
    province = browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[6]/div/div/div[1]/span/span/i')
    sleep(randint(1,3))
    #com_ID_Province chỉ dùng cho Hàn Quốc
    #browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[6]/div/div/div[2]/div/div[1]/ul/li[' + str(com_ID_province) + ']').click()
    province.click()
    sleep(0.8123)
    province.send_keys(str(com_province))
    sleep(1)
    province.send_keys(Keys.ARROW_DOWN)
    province.send_keys(Keys.ENTER)
    sleep(randint(4,7))

###Select City
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[7]/div/div/div[1]/span/span/i')\
                .click()
    sleep(randint(1,3))
    #City có thể chọn random
    '''
    city = browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[7]/div/div/div[1]/input')
    city.send_keys(str(com_district))
    sleep(1)
    city.send_keys(Keys.ARROW_DOWN)
    city.send_keys(Keys.ENTER)'''

###Fill Next
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[2]/div[8]/div/div[1]/input')\
            .send_keys(com_zipcode)
    sleep(0.8231)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[3]/div[2]/div/div[1]/input')\
            .send_keys(com_boss)
    sleep(0.412)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[4]/div/div[3]/div/div/input')\
            .send_keys(com_ID)
    sleep(1.1)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[5]/div/div[3]/div/div[1]/input')\
            .send_keys(com_ID)
    sleep(0.9)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[5]/div/div[4]/div/div/input')\
            .send_keys(com_name_Eng)
    sleep(1.231)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[5]/div/div[5]/div/div/input')\
            .send_keys(com_phone)
    sleep(1.31)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[5]/div/div[6]/div/div/input')\
            .send_keys(com_boss)

###Select Picture
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[5]/div/div[7]/div/div[1]/div').click()
    sleep(1)
    os.startfile(r'C:\Users\Darren\Desktop\Python\choosefile.exe')
    sleep(20)

###Submit
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[7]/button').click()
    sleep(10)
###Verify Now
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/div/i').click()
    wait('Verify Now')
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[8]/div/button').click()
    sleep(1,123)
    browser.find_element_by_xpath('/html/body/div[1]/section/div[2]/section/div/div/section/div[2]/form/div[8]/div/div[1]/span[2]').click()
    sleep(2.14124)

###Check Status
    while True:
        source = str(browser.page_source)
        print(source)
        if (source.find('Your account is being verified') >= 0) or (source.find('Under Review') >= 0):
            print('Reloading...')
            browser.refresh()
            sleep(10)
        else:
            print(re.search(r'''class="status-icon is-active"></i>
      (.*?)!
    </span>''', source).group(1))
            print(re.search(r'class="status-icon status-info"></i> <span>(.*?)</span> <!---->', source).group(1))
            break
    browser.find_element_by_xpath('/html/body/header/div/div[1]/div[2]/ul/li[1]/div/span').click()

    break