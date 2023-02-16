import telepot


API_BOT = '5735408612:AAERpJsMD1Y0B5qGBHFO5iHYuw8_9VGVFYw'
bot = telepot.Bot(API_BOT)


def EnviarMensagemTelegram(mensagem):
    bot.sendMessage(1484986922, mensagem)








