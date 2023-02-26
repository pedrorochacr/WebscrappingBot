from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
import os
from selenium import webdriver

import telepot


API_BOT = os.getenv.API_BOT
bot = telepot.Bot(API_BOT)


def EnviarMensagemTelegram(mensagem):
    try:
        bot.sendMessage(os.getenv.CHAT_ID, mensagem)
    except:
        pass

    # Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd_Chrome = webdriver.Chrome(options=options)
wd_Chrome.get("https://webscrapping-bot.vercel.app/data")

time.sleep(15)
dados = wd_Chrome.find_elements(By.CSS_SELECTOR,'tbody.tableRows')[0]

linhas = dados.find_elements(By.CSS_SELECTOR,'td')

market = linhas[0].accessible_name
oddMin = float(linhas[1].accessible_name)
oddMax = float(linhas[2].accessible_name)

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
    if(market == 'OverGols' or market =='Todos' or market == 'UnderGols'):
        try:
            wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/over-under/full-time')
            time.sleep(3)  
            
            wd_Chrome.maximize_window()
            linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')       
            for linha in linhas:
                bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')): 
                    Over = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Under = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    TotalGols = linha.find_elements(By.CSS_SELECTOR,'span.oddsCell__noOddsCell')[0].text
                    if(market == 'OverGols'):
                        if(Over >= oddMin and Over<=oddMax):
                            EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo :{Home} x {Away} \n Over {TotalGols} Gols \n Odd: {Over}')
                    if(market == 'UnderGols'):
                        if(Under >= oddMin and Under<=oddMax):
                            EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo :{Home} x {Away} \n Under {TotalGols} Gols \n Odd: {Under}')
                else:
                    pass     
        except: 
            pass
    #1x2
    if(market == 'Vencedor' or market =='Todos'):
        try:  
            wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
            time.sleep(2)
            
            linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
            
            for linha in linhas:
                bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')): 
                    Odds_H = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_D = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text )
                    Odds_A = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    if(Odds_H >= oddMin and Odds_H<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n {Home} Vence \n Odd: {Odds_H}')
                    if(Odds_A >= oddMin and Odds_H<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n {Away} Vence \n Odd: {Odds_A}')
                    if(Odds_D >= oddMin and Odds_H<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo :{Home} x {Away} \n Empate \n Odd: {Odds_D}')
                else:
                    pass  
        except:
            pass
    if(market == 'AmbasMarcam' or market =='Todos'):
    # Ambas Marcam (BTTS)
        try:
            wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/both-teams-to-score/full-time')
            time.sleep(2)
        
            linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
            for linha in linhas:
                bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')): 
                    BTTS_Yes = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    BTTS_No = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    if(BTTS_Yes >= oddMin and BTTS_Yes<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n Ambas Marcam: Sim \n Odd: {BTTS_Yes}')
                    if(BTTS_No >= oddMin and BTTS_No<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n Ambas Marcam: Não \n Odd: {BTTS_No}')
                    
                else:
                    pass
        except:
            pass  
    if(market == 'HA' or market =='Todos'):
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
                    Handicap_H = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Handicap_A = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    if(Handicap_H >= oddMin and Handicap_H<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n HA:{Handicap} {Home} \n Odd: {Handicap_H}')
                    if(Handicap_A >= oddMin and Handicap_A<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n HA:{Handicap} {Away} \n Odd: {Handicap_A}')
                else:
                    pass
        except:
            pass  
    if(market == 'EH' or market =='Todos'):
        # HANDICAP Europeu
        try:
            wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/european-handicap/full-time')
            time.sleep(2)
            
            linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
                    
            for linha in linhas:
                bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')): 
                    Handicap = linha.find_elements(By.CSS_SELECTOR,'span.oddsCell__noOddsCell')[0].text
                    
                    Handicap_H = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Handicap_X = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    Handicap_A = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    if(Handicap_H >= oddMin and Handicap_H<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n EH:{Handicap} {Home} \n Odd: {Handicap_H}')
                    if(Handicap_X >= oddMin and Handicap_X<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n EH:{Handicap} Empate \n Odd: {Handicap_X}')
                    if(Handicap_A >= oddMin and Handicap_A<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n EH:{Handicap} {Away} \n Odd: {Handicap_A}')
                else:
                    pass
        except:
            pass  
    if(market == 'DuplaChance' or market =='Todos'):
        # Dupla Chance
        try:
            wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/double-chance/full-time')
            time.sleep(2)
            
            linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
                    
            for linha in linhas:
                bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')): 
                    odds_1x = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    odds_12 = linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text
                    odds_x2 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    if(odds_1x >= oddMin and odds_1x<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n Dupla Chance:{Home} ou Empate \n Odd: {odds_1x}')
                    if(odds_12 >= oddMin and odds_12<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n Dupla Chance:{Home} ou {Away} \n Odd: {odds_12}')
                    if(odds_x2 >= oddMin and odds_x2<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n Dupla Chance:{Away} ou Empate \n Odd: {odds_x2}')
                else:
                    pass
        except:
            pass  

    if(market == 'Exato' or market =='Todos'):
        #Placar Exato
        try:
            wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/correct-score/full-time')
            time.sleep(2)
            
            linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
                    
            for linha in linhas:
                bookie = linha.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')): 
                    Placar = linha.find_elements(By.CSS_SELECTOR,'span.oddsCell__noOddsCell')[0].text
                    Odd_Placar = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    if(Placar >= oddMin and Placar<=oddMax):
                        EnviarMensagemTelegram(f'🔥 🔥  Oportunidade 🔥 🔥  \n Jogo : {Home} x {Away} \n Placar:{Placar} \n Odd: {Odd_Placar}')
                else:
                    pass
        except:
            pass  

wd_Chrome.quit()
    



    