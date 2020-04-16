#chrome.exe --remote-debugging-port=9999 --user-data-dir="C;\automation

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")

chrome_driver = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://displate.com')


