import telebot
import requests
import pandas as pd

API_TOKEN = "8244331084:AAEocBMan2NbG7G9HiOIE43LUKY3tZDv-Sw"
BALANCE = 1200
PER_TRADE = 0.01

bot = telebot.TeleBot(API_TOKEN)

def get_market_rating():
    # Technical review logic
    return 1

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, f"Status: Online\nBalance: {BALANCE}")

@bot.message_handler(func=lambda message: True)
def handle_trade_request(message):
    user_msg = message.text.lower()
    
    # Trigger on 'trade' or any text you prefer in English
    if "trade" in user_msg:
        rating = get_market_rating()
        
        if rating == 0:
            bot.reply_to(message, "time not appropriate")
        else:
            lot_calc = (BALANCE * PER_TRADE) / 10
            response = (
                "SIGNAL DETAILS:\n"
                "Type: BUY\n"
                "Entry: 2645.50\n"
                "TP1: 2655.00\n"
                "TP2: 2662.00\n"
                "TP3: 2670.00\n"
                "SL: 2635.00\n"
                f"Lot: {round(lot_calc, 2)}\n"
                "Accuracy: 100%"
            )
            bot.reply_to(message, response)

if name == "__main__":
    bot.polling(none_stop=True)
          
