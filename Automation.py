
#chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from DisplateLinks import Displates
from DisplateLinks import size_choice


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")

chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://displate.com/admin')


'''
email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input')
email.send_keys('jerred.rogero@displate.com')

password = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input')
password.send_keys('Johnch10$')
'''
# Input links and sizes of 1st Displate
displate1 = Displates('https://displate.com/displate/2035793', 'l')
driver.get(displate1.link)
size_choice()


orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/a').click()
sleep(1)
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/ul/li[5]/a').click()


'''
sleep(1)

proceedtocart = driver.find_element_by_xpath('//*[@id="proceedToCart"]').click()

'''