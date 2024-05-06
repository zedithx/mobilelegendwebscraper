import re

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

main_df = pd.DataFrame()
# month number mapping
month_dict = {"Mar": "03", "Apr": "04", "May": "05"}

# First I need to get the team schedules as they are used in the url
schedule_dict = {}
print("Generating MPL results....")
weeks_list = [1, 2, 3, 4, 5, 6, 7]
# iterate through weeks
for week in weeks_list:
    URL = f"https://ph-mpl.com/schedule#week-{week}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    schedule_frame = soup.find(id=f"week-{week}")
    schedule_columns = schedule_frame.find_all("div", "col-lg-4")
    # iterate through dates to get matches of that day
    for column in schedule_columns:
        # retrieve the date first
        date = column.find("div", class_="header-subtitle").text.strip()
        # convert this date to right format
        day, month, year = date.split()
        date_format = f"2024{month_dict[month]}{day}"
        # retrieve the name of two teams from each card
        teams = column.find_all("div", class_="team-name")
        # Initialise empty list with date as key first
        schedule_dict[date_format] = []
        # Iterate through the matchups of the date
        for i in range(0, len(teams), 2):
            team1 = teams[i].text.strip().lower()
            team2 = teams[i+1].text.strip().lower()
            # add teams to a dict to iterate through later for match page
            schedule_dict[date_format].append([team1, team2])

# Iterate through all match dates and specific matches
for date, matches in schedule_dict.items():
    game_list = []
    for match in matches:
        URL = f"https://ph-mpl.com/data/match/{match[0]}-{match[1]}-{date}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        games = soup.find_all("div", id=lambda x: x and x.startswith('game'))
        # iterate through the games
        for game in games:
            frames = game.findAll("td", attrs={"style":"max-width: 30px;"})
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

