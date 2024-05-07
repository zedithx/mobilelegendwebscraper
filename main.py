import re
import time

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

main_df = pd.DataFrame()
# month number mapping
month_dict = {"Mar": "03", "Apr": "04", "May": "05"}

# First I need to get the team schedules as they are used in the url
schedule_dict = {}
print("Generating MPL results....")
weeks_list = [1, 2, 3, 4, 5, 6, 7]

# Iterate through all match dates and specific matches
URL = f"https://liquipedia.net/mobilelegends/MPL/Philippines/Season_13/Regular_Season#Week_1"
from selenium import webdriver
#set chromodriver.exe path
driver = webdriver.Chrome()
#implicit wait
driver.get(URL)
time.sleep(5)

icons = driver.find_elements(By.CLASS_NAME, "brkts-match-info-icon")
time.sleep(2)
ad_popup = driver.find_element(By.ID, "top-ad")
ad_popup.click()
for icon in icons:
    icon.click()
    info_frame = driver.find_element(By.CLASS_NAME, "brkts-popup")
    print(info_frame)
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

