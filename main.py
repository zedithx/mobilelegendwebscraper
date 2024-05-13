import re
import time

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

main_df = pd.DataFrame()
# month number mapping
# First I need to get the team schedules as they are used in the url
print("Generating MPL results....")

# Iterate through all match dates and specific matches
URL = f"https://liquipedia.net/mobilelegends/MPL/Philippines/Season_13/Regular_Season#Week_1"
#set chromodriver.exe path
driver = webdriver.Chrome()
driver.get(URL)

time.sleep(6)
driver.find_element(By.ID, "top-ad").click()
icons = driver.find_elements(By.CLASS_NAME, "brkts-match-info-icon")
icons = icons[0:24]
time.sleep(2)
for icon in icons:
    icon.click()
    info_frame = driver.find_element(By.CLASS_NAME, "brkts-popup")

    # get week

    # get team
    team1_span, team2_span = info_frame.find_elements(By.CLASS_NAME, "name")
    team1, team2 = team1_span.find_element(By.TAG_NAME, "a"), team2_span.find_element(By.TAG_NAME, "a")
    print(team1.get_attribute("innerText"), team2.get_attribute("innerText"))

    # get heroes
    comp1_div, comp2_div = info_frame.find_elements(By.CLASS_NAME, "brkts-popup-body-game")
    comp1 = comp1_div.find_elements(By.TAG_NAME, "a")
    comp2 = comp2_div.find_elements(By.TAG_NAME, "a")
    for hero in comp1:
        pass
        # print(hero.get_attribute("innerText").strip())


    # get W indicator


    # get rid of the popup
    icon.click()

# To access the stats we need to click one by one then put in our df
# iterate through the games
            # heroes = game.findAll(string=re.compile("[A-Za-z]"))
            # print(heroes)

#         df = pd.DataFrame(data)
#         df.insert(0, "Date", np.nan, True)
#         df.loc[0, "Date"] = f"{day}/{month}/{YEAR}"
#         main_df = pd.concat([main_df, df], axis=0)
# main_df.insert(6, "First prize", np.nan)
# main_df.iloc[:len(first_winners), 6] = first_winners
# main_df.to_excel("forfun.xlsx", index=False)
#
# print("Generation has been completed")

