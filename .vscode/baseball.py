#Create soup of baseball page, scrape and manipulate data.

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Instantiate an Options object
# and add the "--headless" argument
opts = Options()
opts.add_argument(" --headless")
# If necessary set the path to you browser’s location
opts.binary_location= 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# Set the location of the webdriver
chrome_driver = 'C:\chromedriver.exe'
# Instantiate a webdriver
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)
# Load the HTML page
driver.get("https://www.espn.com/mlb/team/_/name/nyy/new-york-yankees")

# Put the page source into a variable and create a BS object from it
soup_file=driver.page_source
soup = BeautifulSoup(soup_file, features="lxml")

print(soup.title.get_text())

#Get recent articles about Yankees
for article in soup.find_all('a', class_="realStory", limit=3):
    if("Yank" in article.get_text()):
        print(article.get_text())
        print(article.get('href'))

#Get upcoming game
try:
    upcoming_game = soup.find('a', class_="upcoming").find('div', class_="game-info")

    for child in upcoming_game.children:
        print("Upcoming: " + child)
except:
    print("No upcoming games")

#Get last game played with result
try:
    game_info = soup.find('div', class_="game-info")
    for child in game_info.children:
        played_against = child

    game_result = soup.find('div', class_=re.compile("game-result"))
    for child in game_result.children:
        result = child

    print(played_against, result)
except:
    print("No past games")
