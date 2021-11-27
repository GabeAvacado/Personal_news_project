#Soup 
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Soup:
    # Instantiate an Options object
    opts = Options()
    # and add the "--headless" argument
    opts.add_argument(" --headless")
    # If necessary set the path to you browser’s location
    opts.binary_location= 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # Set the location of the webdriver
    chrome_driver = 'C:\chromedriver.exe'
    # Instantiate a webdriver
    driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)