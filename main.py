import telebot
from telebot import types
import json
import os
from flask import Flask
from threading import Thread

# --- БЛОК ВЕБ-СЕРВЕРА ДЛЯ ХОСТИНГА ---
app = Flask('')
@app.route('/')
def home():
    return "SmolaG жив!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()
# -------------------------------------

TOKEN = '8383819074:AAFRtEPCokze89NvmF14WPATfeeRSzrM-ZU'
bot = telebot.TeleBot(TOKEN)
DB_FILE = "smola_db.json"

user_data = {} # Тут твоя логика загрузки/сохранения из прошлых сообщений

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает 24/7!")

# Запуск
if __name__ == "__main__":
    keep_alive() # Запускаем "приманку" для хостинга
    print("Бот стартовал...")
    bot.infinity_polling()