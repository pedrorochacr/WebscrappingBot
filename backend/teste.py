from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from tqdm import tqdm
import os
from selenium import webdriver
from bs4 import BeautifulSoup



import telepot


API_BOT = '5735408612:AAERpJsMD1Y0B5qGBHFO5iHYuw8_9VGVFYw'
bot = telepot.Bot(API_BOT)


def EnviarMensagemTelegram(mensagem):
    try:
        print("Nsas")
        bot.sendMessage(1484986922, mensagem)
    except:
        print("excecao")

    # Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd_Chrome = webdriver.Chrome(options=options)
wd_Chrome.get("https://www.flashscore.com/")
time.sleep(3)




calendario = wd_Chrome.find_element(By.CSS_SELECTOR,'div.calendarCont')
calendario.find_element(By.CSS_SELECTOR,'button.calendar__navigation.calendar__navigation--tomorrow').click()
time.sleep(3)
id_jogos = []
jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')

for i in jogos:
    id_jogos.append(i.get_attribute("id"))

# Exemplo de ID de um jogo: 'g_1_Gb7buXVt'    
id_jogos = [i[4:] for i in id_jogos]

# Pegando as Informacoes Básicas do Jogo
for link in tqdm(id_jogos, total=len(id_jogos)):
    wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/match-summary')
    
    try:
        Date = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[0]
        Time = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[1]
        Country = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country').text.split(':')[0]
        League = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country')
        League = League.find_element(By.CSS_SELECTOR,'a').text
        Home = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__home')
        Home = Home.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
        Away = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__away')
        Away = Away.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
    except:
        pass
    # Mais ou Menos Gols
    try:
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/over-under/full-time')
        time.sleep(3)  
        
        wd_Chrome.maximize_window()
        linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')       
        print(Home)
        
        for linha in linhas:
            Over = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
            Under = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text
            TotalGols = linha.find_elements(By.CSS_SELECTOR,'span.oddsCell__noOddsCell')[0].text
            EnviarMensagemTelegram(f'Jogo :{Home} x {Away} Gols: Over :{Over} Under: {Under}')
            bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
            bookie = bookie.get_attribute('title')
            print(bookie)
            break
            
        break  
    except Exception as e: 
        print(e)
        break
# Match Odds
    try:  
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
        time.sleep(2)
        
        linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        for linha in linhas:
            bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
            bookie = bookie.get_attribute('title')
            if ((bookie == 'bet365')): 
                Odds_H = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                Odds_D = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text 
                Odds_A = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text
        
            else:
                pass


                
    except:
        pass

# Ambas Marcam (BTTS)
    try:
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/both-teams-to-score/full-time')
        time.sleep(2)
    
        linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
                

        for linha in linhas:
            bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
            bookie = bookie.get_attribute('title')
            if ((bookie == 'bet365')): 
                BTTS_Yes = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                BTTS_No = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text
        
            else:
                pass
    except:
        pass  

# HANDICAP ASIÁTICO 
    try:
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/asian-handicap/full-time')
        time.sleep(2)
        
        linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
                
        for linha in linhas:
            bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
            bookie = bookie.get_attribute('title')
            if ((bookie == 'bet365')): 
                Handicap = linha.find_elements(By.CSS_SELECTOR,'span.oddsCell__noOddsCell')[0].text
                Handicap_H = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                Handicap_A = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text
            else:
                pass
    except:
        pass  

wd_Chrome.quit()
    



    