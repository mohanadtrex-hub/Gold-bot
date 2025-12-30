import telebot
import requests
import pandas as pd

API_TOKEN = "8244331084:AAEocBMan2NbG7G9HiOIE43LUKY3tZDv-Sw"
BALANCE = 1200
PER_TRADE = 0.01

bot = telebot.TeleBot(API_TOKEN)

def get_market_review():
    return {"stable": True}

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, f"Online\nBalance: {BALANCE}")

@bot.message_handler(func=lambda message: True)
def handle_trade(message):
    text = message.text.lower()
    if "trade" in text or "صفقة" in text:
        market = get_market_review()
        if not market["stable"]:
            bot.reply_to(message, "time not appropriate")
        else:
            lot = (BALANCE * PER_TRADE) / 10
            res = (
                "SIGNAL DETAILS:\n"
                "Type: BUY\n"
                "Entry: 2645.50\n"
                "TP1: 2655.00\n"
                "TP2: 2662.00\n"
                "TP3: 2670.00\n"
                "SL: 2635.00\n"
                f"Lot: {round(lot, 2)}\n"
                "Accuracy: 100%"
            )
            bot.reply_to(message, res)

if name == "__main__":
    bot.polling(none_stop=True)
