#chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation
from Displate import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://displate.com/admin')

'''
email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input')
email.send_keys()

password = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input')
password.send_keys()
'''

# clicks through admin portal
orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/a').click()
sleep(1)
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[7]/ul/li[5]/a').click()


cart = 1
while cart <= 3:  # Enter Quantity of Displates
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

#Gets you through checkout back to admin panel
sleep(1)
proceedToCart = driver.find_element_by_xpath('//*[@id="proceedToCart"]').click()
sleep(1)
checkout = driver.find_element_by_xpath('//*[@id="checkout-btn-ab1"]').click()
createInternal = driver.find_element_by_xpath('//*[@id="react-checkout"]/div/div[2]/div[2]/div/button').click()
sleep(1)

# Shipping Info
email = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[1]/div[2]/input')
email.clear()
email.send_keys(info.email)

phone = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[2]/div[2]/input')
phone.clear()
phone.send_keys(info.phone)

name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[3]/div[2]/input')
name.clear()
name.send_keys(info.name)

address1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[5]/div[2]/input')
address1.clear()
address1.send_keys(info.address1)

address2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[6]/div[2]/input')
address2.clear()
address2.send_keys(info.address2)

city = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[7]/div[2]/input')
city.clear()
city.send_keys(info.city)

state = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[8]/div[2]/input')
state.clear()
state.send_keys(info.state)

zip_code = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[9]/div[2]/input')
zip_code.clear()
zip_code.send_keys(info.zip_code)





