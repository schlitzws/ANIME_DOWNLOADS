###The below assumes you have already installed python 3..###
<<<<<<< HEAD

###In order for you to use this script you will need to install the selenium library.

###The easiest way for you to do this is to use pip in powershell/linux/Mac: pip install selenium

###(not exactly sure about the Mac, please do your own research.)

###once that is done you have to install a webdriver from googlechrome, firefox, edge, or ie.

###put the path to the file in your env variables ### windows

###put the path in your ~/.profile file in your home dir ### linux

=======
###In order for you to use this script you will need to install the selenium library.
###The easiest way for you to do this is to use pip in powershell/linux/Mac: pip install selenium 
###(not exactly sure about the Mac, please do your own research.)
###once that is done you have to install a webdriver from googlechrome, firefox, edge, or ie.
###put the path to the file in your env variables ### windows
###put the path in your ~/.profile file in your home dir ### linux
>>>>>>> 1dee114c8dbaf75f0a183d2cf35c305b53a2dad1
###might be the same as above for mac but I'm not entirely sure.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def download():
##    chrome_options = Options()
##    chrome_options.add_argument("--headless")
##    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    target_anime = input("Please enter the name of the anime you want delimited by '-' character like :: battle-programmer-shirase")
    url = "https://anime.thehylia.com/downloads/series/" + target_anime
    driver.get(url)
    time.sleep(3)
    ed = driver.find_elements_by_class_name("episode_download")
    for i in ed:
        if i.text == "Download":
            i.click()
            time.sleep(15)
    driver.quit()

def listAnime():
##    chrome_options = Options()
##    chrome_options.add_argument("--headless")
##    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    url = "https://anime.thehylia.com/downloads/browse/all"
    driver.get(url)
    #anime_list = driver.find_element_by_xpath('//*[@id="content_container"]/div[2]/table/tbody/tr/td/div/p[1]')
    anime_list = driver.find_elements_by_css_selector("#content_container > div.floatbox > table > tbody > tr > td > div > p:nth-child(2) > a")
    #a = driver.find_elements_by_tag_name("a")
    print( """
    Before listing Anime, please note in order for you to download the anime you will need to know the URI after /series/ in the listed anime.
    """)
    time.sleep(10)
    counter = 0
    for i in anime_list:
##        if i != "[MP3]" or i != "[FLAC+MP3]":
        print(i.text)
        print(i.get_attribute("href"))
        counter += 1
        if counter > 20:
            input("Press enter to continue viewing 20 more Anime.")
            counter = 0
            if input("Have you found your Anime of choice input letter b to go back to the main menu otherwise press enter.") == "b":
                break
    driver.quit()

while(True):
    init_input = input("Please input what you would like to do next, h for the help.")
    if init_input == "h":
        print("""

            Help Menu for Need Anime Program - Written by SWS

            This program is used to list, download, or watch anime from https://anime.thehylia.com/.

           h key - Display this menu.
           l key - Displays a list of anime depending on the args supplied.
           d key - Downloads the anime from the target anime that you input.
           w key - Watches the anime from the target anime that you input.
           q key - To quit the program.

        """)
    elif init_input == "l":
        listAnime()
    elif init_input == "d":
        download()
    elif init_input == "q":
        print("Exiting program..")
        time.sleep(3)
        quit()
    elif init_input == "":
        print("Please input a specic key per the help menu, press h key for help")
