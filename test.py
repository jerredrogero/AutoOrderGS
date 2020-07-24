# chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
#chrome_driver = "C:\selenium\chromedriver.exe"
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
def m():
    driver.find_element_by_xpath('//*[@id="product-size"]/div/label[1]/div').click()
def l():
    driver.find_element_by_xpath('//*[@id="product-size"]/div/label[2]/div').click()    
def xl():
    driver.find_element_by_xpath('//*[@id="product-size"]/div/label[3]/div').click()
def gloss():
    driver.find_element_by_xpath('//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[2]/div[1]/div[2]/label[2]').click()
def autoOrder1():
    displate1 = config['displate1']
    driver.get(displate1)
    size1 = config['size1']
    finish1 = config['finish1']
    if config['size1'] == 'm':
        m()
    if config['size1'] == 'l':
        l()
    if config['size1'] == 'xl':
        xl()
    if finish1 =='yes':
        gloss()
def autoOrder2():
    displate2 = config['displate2']
    driver.get(displate2)
    size2 = config['size2']
    finish2 = config['finish2']
    if config['size2'] == 'm':
        m()
    if config['size2'] == 'l':
        l()
    if config['size2'] == 'xl':
        xl()
    if finish2 =='yes':
        gloss()
def autoOrder3():
    displate3 = config['displate3']
    driver.get(displate3)
    size3 = config['size3']
    finish3 = config['finish3']
    if config['size3'] == 'm':
        m()
    if config['size3'] == 'l':
        l()
    if config['size3'] == 'xl':
        xl()
    if finish3 =='yes':
        gloss()
def autoOrder4():
    displate4 = config['displate4']
    driver.get(displate4)
    size4 = config['size4']
    finish4 = config['finish4']
    if config['size4'] == 'm':
        m()
    if config['size4'] == 'l':
        l()
    if config['size4'] == 'xl':
        xl()
    if finish4 =='yes':
        gloss()
def autoOrder5():
    displate5 = config['displate5']
    driver.get(displate5)
    size5 = config['size5']
    finish5 = config['finish5']
    if config['size5'] == 'm':
        m()
    if config['size5'] == 'l':
        l()
    if config['size5'] == 'xl':
        xl()
    if finish5 =='yes':
        gloss()
def autoOrder6():
    displate6 = config['displate6']
    driver.get(displate6)
    size6 = config['size6']
    finish6 = config['finish6']
    if config['size6'] == 'm':
        m()
    if config['size6'] == 'l':
        l()
    if config['size6'] == 'xl':
        xl()
    if finish6 =='yes':
        gloss()
def autoOrder7():
    displate7 = config['displate7']
    driver.get(displate7)
    size7 = config['size7']
    finish7 = config['finish7']
    if config['size7'] == 'm':
        m()
    if config['size7'] == 'l':
        l()
    if config['size7'] == 'xl':
        xl()
    if finish7 =='yes':
        gloss()
def autoOrder8():
    displate8 = config['displate8']
    driver.get(displate8)
    size8 = config['size8']
    finish8 = config['finish8']
    if config['size8'] == 'm':
        m()
    if config['size8'] == 'l':
        l()
    if config['size8'] == 'xl':
        xl()
    if finish8 =='yes':
        gloss()
def autoOrder9():
    displate9 = config['displate9']
    driver.get(displate9)
    size9 = config['size9']
    finish9 = config['finish9']
    if config['size9'] == 'm':
        m()
    if config['size9'] == 'l':
        l()
    if config['size9'] == 'xl':
        xl()
    if finish9 =='yes':
        gloss()
def autoOrder10():
    displate10 = config['displate10']
    driver.get(displate10)
    size10 = config['size10']
    finish10 = config['finish10']
    if config['size10'] == 'm':
        m()
    if config['size10'] == 'l':
        l()
    if config['size10'] == 'xl':
        xl()
    if finish10 =='yes':
        gloss()
def autoOrder11():
    displate11 = config['displate11']
    driver.get(displate11)
    size11 = config['size11']
    finish11 = config['finish11']
    if config['size11'] == 'm':
        m()
    if config['size11'] == 'l':
        l()
    if config['size11'] == 'xl':
        xl()
    if finish11 =='yes':
        gloss()
def autoOrder12():
    displate12 = config['displate12']
    driver.get(displate12)
    size12= config['size12']
    finish12 = config['finish12']
    if config['size12'] == 'm':
        m()
    if config['size12'] == 'l':
        l()
    if config['size12'] == 'xl':
        xl()
    if finish12 =='yes':
        gloss()
def autoOrder13():
    displate13 = config['displate13']
    driver.get(displate13)
    size13 = config['size13']
    finish13 = config['finish13']
    if config['size13'] == 'm':
        m()
    if config['size13'] == 'l':
        l()
    if config['size13'] == 'xl':
        xl()
    if finish13 =='yes':
        gloss()
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
    if cart == 11:
        autoOrder11()
    if cart == 12:
        autoOrder12()
    if cart == 13:
        autoOrder13()
    addToCart = driver.find_element_by_xpath('//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[3]/div[1]/button').click()
    cart += 1

proceedToCart = driver.find_element_by_link_text('Proceed to cart').click()
checkout = driver.find_element_by_link_text('Checkout').click()

# So the internal name isn't autofilled
nameCheckout = driver.find_element_by_xpath('//*[@id="inputShippingFirstName"]')
nameCheckout.clear()
nameCheckout.send_keys(config['Name'])

# FIX THIS
createInternal = driver.find_element_by_class_name('button button--primary button--full-width')
sleep(5)
createInternal.click()

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