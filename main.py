import telebot
from telebot import types
import json
import os

# Твой токен уже здесь
TOKEN = '8383819074:AAFRtEPCokze89NvmF14WPATfeeRSzrM-ZU'
bot = telebot.TeleBot(TOKEN)
DB_FILE = "smola_db.json"

# Загрузка данных
def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

# Сохранение данных
def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

user_data = load_data()

@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data:
        user_data[user_id] = 0
        save_data(user_data)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🌲 Добыть Смолу")
    btn2 = types.KeyboardButton("⚗️ Мой баланс")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, f"Привет! Это SmolaG. Нажимай на кнопки, чтобы фармить!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🌲 Добыть Смолу")
def farm(message):
    user_id = str(message.from_user.id)
    user_data[user_id] = user_data.get(user_id, 0) + 1
    save_data(user_data)
    bot.send_message(message.chat.id, f"Капля получена! Всего смолы: {user_data[user_id]}")

@bot.message_handler(func=lambda message: message.text == "⚗️ Мой баланс")
def balance(message):
    current_balance = user_data.get(str(message.from_user.id), 0)
    bot.send_message(message.chat.id, f"Твой баланс: {current_balance} Смолы")

print("Бот запущен...")
bot.infinity_polling()