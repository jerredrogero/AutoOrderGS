
#chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from DisplateLinks import Displates

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")

chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://displate.com/admin')



email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input')
email.send_keys('jerred.rogero@displate.com')

password = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input')
password.send_keys('Johnch10$')



orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/a').click()
sleep(1)
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/ul/li[5]/a').click()

displate1 = Displate('https://displate.com/displate/362246', 'medium')

print(displate1.size)
