# chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9999

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Submissions').sheet1

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
#chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome("C:\selenium\chromedriver.exe", options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://displate.com/admin')

def nameF():
   return sheet.cell(2,1).value
name = nameF()
def emailF():
    return sheet.cell(2,3).value
email = emailF()
def phoneF():
    return sheet.cell(2,4).value
phone = phoneF()
def countryF():
    return sheet.cell(2,5).value
country = countryF()
def address1F():
    return sheet.cell(2,6).value
address1 = address1F()
def address2F():
    return sheet.cell(2,7).value
address2 = address2F()
def cityF():
    return sheet.cell(2,8).value
city = cityF()
def stateF():
    return sheet.cell(2,9).value
state = stateF()
def postalF():
    return sheet.cell(2,10).value
postal = postalF()
def displateF():
    return sheet.cell(2,11).value
displate = displateF()
def sizeF():
    return sheet.cell(2,15).value
size = sizeF()
def m():
    driver.find_element_by_xpath('//*[@id="product-size"]/div/label[1]/div').click()
def l():
    driver.find_element_by_xpath('//*[@id="product-size"]/div/label[2]/div').click()    
def xl():
    driver.find_element_by_xpath('//*[@id="product-size"]/div/label[3]/div').click()
def gloss():
    driver.find_element_by_xpath('//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[2]/div[1]/div[2]/label[2]').click()

def autoOrder():
    driver.get(displate)
    if size == 'm' or size == 'M':
        m()
    if size == 'l' or size == 'L':
        l()
    if size == 'xl' or size == 'XL':
        xl()

# Clicks through admin portal
orders = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/a').click()
createnew = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/ul/li[5]/a').click()

autoOrder()

addToCart = driver.find_element_by_xpath('//*[@id="react-product-page"]/div/div[1]/section/div[2]/div[3]/div[1]/button').click()
proceedToCart = driver.find_element_by_link_text('Proceed to cart').click()
checkout = driver.find_element_by_link_text('Checkout').click()

# Shipping Info
nameCheckout = driver.find_element_by_xpath('//*[@id="inputShippingFirstName"]')
nameCheckout.send_keys(name)
address1Checkout = driver.find_element_by_xpath('//*[@id="inputShippingAddress1"]')
address1Checkout.send_keys(address1)
postalCheckout = driver.find_element_by_xpath('//*[@id="inputShippingPostal"]')
postalCheckout.send_keys(postal)
phoneCheckout = driver.find_element_by_xpath('//*[@id="checkout_form"]/div/div[8]/div/input')
phoneCheckout.send_keys(phone)
address2Checkout = driver.find_element_by_xpath('//*[@id="inputShippingAddress2"]')
try: 
    address2Checkout.send_keys(address2)
except:
    pass
cityCheckout = driver.find_element_by_xpath('//*[@id="inputShippingCity"]')
cityCheckout.send_keys(city)
stateCheckout = driver.find_element_by_xpath('//*[@id="inputShippingState"]')
stateCheckout.send_keys(state)
pprint(phone)
pprint(email)

sheet.delete_rows(2)

#TODO: implement some try and excepts for checkout