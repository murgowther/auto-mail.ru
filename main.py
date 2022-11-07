import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
EXE_PATH = 'chromedriver.exe'
EMAIL = "your_email"
PASSWORD = "your_password"

browser = webdriver.Chrome(executable_path=EXE_PATH)
site = browser.get('https://e.mail.ru/templates/')
#e-mail
emailElem = browser.find_element(By.NAME, 'username')
emailElem.send_keys(EMAIL)
emailElem.submit()
time.sleep(3)
#пароль
passwordElem = browser.find_element(By.NAME, 'password')
passwordElem.send_keys(PASSWORD)
passwordElem.submit()
time.sleep(3)


with open('email_list.csv', encoding="utf-8") as file:
    EMAIL_LIST = csv.reader(file)
    i=0
    # Запускаем цикл
    for row in EMAIL_LIST:
        try:
            email_to = row[0]
            # Нажимаем кнопку шаблоны (первый в списке шаблон настраиваем заранее)
            browser.find_element(By.XPATH,
                '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/a[1]').click()
            time.sleep(1)
            # Заполняем поле кому
            browser.find_element(By.CLASS_NAME, 'container--zU301').send_keys(email_to)#email_to
            time.sleep(1)
            #Нажимаем кнопку отправить
            browser.find_element(By.CLASS_NAME, 'base-0-2-14.primary-0-2-28.small-0-2-23').click()
            time.sleep(1)
            browser.refresh()
            time.sleep(1)
            i += 1

        except Exception:
            print("Error")
            time.sleep(30)
            # # Снова нажимаем кнопку отправить
            browser.find_element(By.CLASS_NAME, 'base-0-2-14.primary-0-2-28.small-0-2-23').click()
            time.sleep(3)
            browser.refresh()
            time.sleep(2)
            i+=1

