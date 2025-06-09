import os
import telebot
from dotenv import load_dotenv
from services.llm_provider import LLM_PROVIDER

load_dotenv()

class Main():

    def __init__(self):
        self.bot = telebot.TeleBot(os.getenv("TELEGRAM_KEY"))
        self.bot.message_handler(func=lambda message: True)(self.echo_message)

    def echo_message(self, message):
        openai = LLM_PROVIDER()
        mensagem = openai.send_message(message.text)
        self.bot.reply_to(message, mensagem)

    def start(self):
        print("Ligado...")
        self.bot.polling()

if __name__ == '__main__':
    meu_bot = Main()
    meu_bot.start()

    