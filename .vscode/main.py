import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# Instantiate an Options object
# and add the "--headless" argument
opts = Options()
opts.add_argument(" --headless")
# If necessary set the path to you browser’s location
opts.binary_location= 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# Set the location of the webdriver
# Automatically install and use newest chrome driver
chrome_driver = ChromeDriverManager().install()
# Instantiate a webdriver
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)
# Load the HTML page
driver.get("https://www.espn.com/mlb/team/_/name/nyy/new-york-yankees")

# Amount of articles wanting to retrieve
# Don't want to use limit parameter since it'll retrieve videos. Want only articles
article_limit = 3

# Put the page source into a variable and create a BS object from it
soup_file=driver.page_source
soup = BeautifulSoup(soup_file, features="lxml")

print(soup.title.get_text())

#Get recent articles about Yankees
for article in soup.find_all('h2', class_="contentItem__title"):
    # Only get 3 articles that match critera
    if (article_limit <= 0):
        break
    #Skip any videos
    if (article.parent.parent.get('href') == None):
            continue
    #Article title must contain string "Yank"
    if("Yank" in article.get_text()):
        print(article.get_text())
        href = article.parent.parent.get('href')
        article_link = "espn.com{}".format(href)
        print(article_link)
        article_limit = article_limit - 1
    else:
        continue


#TODO: Getting upcoming and past games no longer works. ESPN site has been updated. Current html tags don't exist
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
