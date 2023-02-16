import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import telepot


API_BOT = '5735408612:AAERpJsMD1Y0B5qGBHFO5iHYuw8_9VGVFYw'
bot = telepot.Bot(API_BOT)

def send_message_to_telegram(message):
    bot.sendMessage(1484986922, message)

def get_game_info(link):
    url = f"https://www.flashscore.com/match/{link}/#/match-summary"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    Date = soup.select_one("div.duelParticipant__startTime").text.split(" ")[0]
    Time = soup.select_one("div.duelParticipant__startTime").text.split(" ")[1]
    Country = soup.select_one("span.tournamentHeader__country").text.split(":")[0]
    League = soup.select_one("span.tournamentHeader__country a").text
    Home = soup.select_one("div.duelParticipant__home div.participant__participantName").text
    Away = soup.select_one("div.duelParticipant__away div.participant__participantName").text
    
    return {"Date": Date, "Time": Time, "Country": Country, "League": League, "Home": Home, "Away": Away}


url = "https://www.flashscore.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# find the button to navigate to next day
calendar_button = soup.select_one('div.calendarCont button.calendar__navigation.calendar__navigation--tomorrow')
calendar_url = calendar_button.get("onclick")[17:-2]
calendar_url = "https://www.flashscore.com" + calendar_url

res = requests.get(calendar_url)
soup = BeautifulSoup(res.text, "html.parser")

# find all scheduled games
games = soup.select("div.event__match--scheduled")
game_ids = [game.get("id")[4:] for game in games]

game_infos = []
for link in game_ids:
    game_infos.append(get_game_info(link))

df = pd.DataFrame(game_infos)

url = f"https://www.flashscore.com/match/{game_ids[0]}/#/odds-comparison/over-under/full-time"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

rows = soup.select("div.ui-table__row")
for row in rows:
    bookie = row.select_one("img.prematchLogo").get("title")
    if bookie == "bet365":
        Over = row