from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from os import system
import logging 

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

def create(name):

    bot = ChatBot(name = name,
                  read_only = False,                  
                  logic_adapters = ["chatterbot.logic.BestMatch", "chatterbot.logic.TimeLogicAdapter"],                 
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")

    return bot


def train(bot):

    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')


def startchat(bot):

    system('clear')
    print("Hello, I am Jordan. How can I help you")
    bye = ["bye jordan", "bye", "good bye"] 
    
    while (True):
        user_input = input("me: ")   
        if user_input.lower() in bye:
            print("Jordan: Good bye and have a blessed day!")
            break
        
        response = bot.get_response(user_input)
        print("Jordan:", response)


bot = create('somtobot')
train(bot)
startchat(bot)