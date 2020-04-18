#chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
from Displate import *


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")

chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://displate.com')
'''
email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input')
email.send_keys()

password = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input')
password.send_keys()


# clicks through admin portal
orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/a').click()
sleep(1)
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/ul/li[5]/a').click()
'''

cart = 1
while cart <= 3:  # Enter Quanity of Displates HERE
    if cart == 1:
        driver.get(displate1.link)
        if displate1.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
        if displate1.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
        if displate1.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
    if cart == 2:
        driver.get(displate2.link)
        if displate2.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
        if displate2.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
        if displate2.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
    if cart == 3:
        driver.get(displate3.link)
        if displate3.size == 'm':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
        if displate3.size == 'l':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
        if displate3.size == 'xl':
            driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
    sleep(1)
    addToCart = driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
    cart += 1
sleep(.5)
proceedToCart = driver.find_element_by_xpath('//*[@id="proceedToCart"]').click()
checkout = driver.find_element_by_xpath('//*[@id="checkout-btn-ab1"]').click()

# Shipping Info

first = driver.find_element_by_xpath('//*[@id="inputShippingFirstName"]')
first.clear()
first.send_keys(info.first)

last = driver.find_element_by_xpath('//*[@id="inputShippingLastName"]')
last.clear()
last.send_keys(info.last)

address1 = driver.find_element_by_xpath('//*[@id="inputShippingAddress1"]')
address1.clear()
address1.send_keys(info.address1)

address2 = driver.find_element_by_xpath('//*[@id="inputShippingAddress2"]')
address2.clear()
address2.send_keys(info.address2)

zip = driver.find_element_by_xpath('//*[@id="inputShippingPostal"]')
zip.clear()
zip.send_keys(info.zip)

city = driver.find_element_by_xpath('//*[@id="inputShippingCity"]')
city.clear()
city.send_keys(info.city)

state = driver.find_element_by_xpath('//*[@id="checkout_form"]/div/div[6]/div/div/div[1]')
state.send_keys(info.state)

'''
phone = driver.find_element_by_xpath('//*[@id="checkout_form"]/div/div[8]/div/input')
phone.clear()
state.send_keys(info.phone)
'''
sleep(1)
proceedtocart = driver.find_element_by_xpath('//*[@id="proceedToCart"]').click()
