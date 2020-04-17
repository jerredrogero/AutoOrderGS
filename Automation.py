#chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from Displate import Displate
from Displate import


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")

chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://displate.com')
'''
email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input')
email.send_keys('jerred.rogero@displate.com')

password = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input')
password.send_keys()


# click through admin portal

orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/a').click()
sleep(1)
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/ul/li[5]/a').click()
'''

# Enter Displate Links and Sizes Here

displate1 = Displate('https://displate.com/displate/2035793', 'l')
displate2 = Displate('https://displate.com/displate/362246', 'xl')
displate3 = Displate('https://displate.com/displate/1368789', 'm')

cart = 1

while cart <= 3:  # Enter Quanity of Product
    if cart == 1:
        driver.get(displate1.link)
        if displate1.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]/img').click()
        if displate1.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]/img').click()
        if displate1.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]/img').click()
    if cart == 2:
        driver.get(displate2.link)
        if displate2.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]/img').click()
        if displate2.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]/img').click()
        if displate2.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]/img').click()
    if cart == 3:
        driver.get(displate3.link)
        if displate3.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]/img').click()
        if displate3.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]/img').click()
        if displate3.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]/img').click()

    addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
    cart += 1
checkout = driver.find_element_by_xpath('//*[@id="checkout-btn-ab1"]').click()













'''
sleep(1)

proceedtocart = driver.find_element_by_xpath('//*[@id="proceedToCart"]').click()

'''