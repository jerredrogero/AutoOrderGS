# chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml
          
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://displate.com/admin')

'''
email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input')
email.send_keys()

password = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input')
password.send_keys()
'''

# Clicks through admin portal
orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/a').click()
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/ul/li[5]/a').click()
    
with open ('config.yml', 'r') as stream:
    config = yaml.safe_load(stream)

def autoOrder1():
    displate1 = config['displate1']
    driver.get(displate1)
    size1 = config['size1']
    if config['size1'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size1'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size1'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder2():
    displate2 = config['displate2']
    driver.get(displate2)
    size2 = config['size2']
    if config['size2'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size2'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size2'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder3():
    displate3 = config['displate3']
    driver.get(displate3)
    size3 = config['size3']
    if config['size3'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size3'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size3'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder4():
    displate4 = config['displate4']
    driver.get(displate4)
    size4 = config['size4']
    if config['size4'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size4'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size4'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder5():
    displate5 = config['displate5']
    driver.get(displate5)
    size5 = config['size5']
    if config['size5'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size5'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size5'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder6():
    displate6 = config['displate6']
    driver.get(displate6)
    size6 = config['size6']
    if config['size6'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size6'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size6'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder7():
    displate7 = config['displate7']
    driver.get(displate7)
    size7 = config['size7']
    if config['size7'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size7'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size7'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder8():
    displate8 = config['displate8']
    driver.get(displate8)
    size8 = config['size8']
    if config['size8'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size8'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size8'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder9():
    displate9 = config['displate9']
    driver.get(displate9)
    size9 = config['size9']
    if config['size9'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size9'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size9'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()
def autoOrder10():
    displate10 = config['displate10']
    driver.get(displate10)
    size10 = config['size10']
    if config['size10'] == 'm':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[1]/div[2]').click()
    if config['size10'] == 'l':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[2]/div[2]').click()
    if config['size10'] == 'xl':
        driver.find_element_by_xpath('//*[@id="product-size"]/div[2]/div[3]/div[2]').click()

cart = 1     
while cart <= config['Displates']:    
    if cart == 1:
        autoOrder1()
    if cart == 2:
        autoOrder2()
    if cart == 3:
        autoOrder3()
    if cart == 4:
        autoOrder4()
    if cart == 5:
        autoOrder5()
    if cart == 6:
        autoOrder6()
    if cart == 7:
        autoOrder7()
    if cart == 8:
        autoOrder8()
    if cart == 9:
        autoOrder9()
    if cart == 10:
        autoOrder10()
    addToCart = driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
    cart += 1

proceedToCart = driver.find_element_by_xpath('//*[@id="proceedToCart"]').click()
checkout = driver.find_element_by_xpath('//*[@id="checkout-btn-ab1"]').click()

# So the internal name isn't autofilled
nameCheckout = driver.find_element_by_xpath('//*[@id="inputShippingFirstName"]')
nameCheckout.clear()
nameCheckout.send_keys(config['Name'])

createInternal = driver.find_element_by_xpath('//*[@id="react-checkout"]/div/div[2]/div[2]/div/button').click()

# Shipping Info
email = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[1]/div[2]/input')
email.clear()
email.send_keys(config['Email'])

phone = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[2]/div[2]/input')
phone.clear()
phone.send_keys(config['Phone'])

name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[3]/div[2]/input')
name.clear()
name.send_keys(config['Name'])

address1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[5]/div[2]/input')
address1.clear()
address1.send_keys(config['Address1'])

address2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[6]/div[2]/input')
address2.clear()
try: 
    address2.send_keys(config['Address2'])
except:
    pass

city = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[7]/div[2]/input')
city.clear()
city.send_keys(config['City'])

state = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[8]/div[2]/input')
state.clear()
state.send_keys(config['State'])

zip_code = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[4]/form/div[9]/div[2]/input')
zip_code.clear()
zip_code.send_keys(config['Postal'])

'''
TODO:
figure out pyinstaller outside files
Bundle into Docker

'''