import telebot
import datetime

# --- إعدادات البوت ---
API_TOKEN = '7611986423:AAH_Ff6u6p7h9X4C9_wN3_qZ-mK4eR_xY' 
USER_BALANCE = 1200  
RISK_PER_TRADE = 0.01  

bot = telebot.TeleBot(API_TOKEN)

def get_market_rating():
    rating = 85  
    if rating < 75:
        return "unstable", rating
    return "stable", rating

def calculate_params(balance, risk_pc):
    entry = 2650.00
    tp = entry + 10.0
    sl = entry - 5.0
    lot = (balance * risk_pc) / 500
    return entry, tp, sl, round(lot, 2)

@bot.message_handler(commands=['start', 'check'])
def handle_message(message):
    status, rate = get_market_rating()
    if status == "unstable":
        bot.reply_to(message, f"⚠️ Current state: time not appropriate\nRating: {rate}%")
    else:
        entry, tp, sl, lot = calculate_params(USER_BALANCE, RISK_PER_TRADE)
        msg = f"✅ **Market Stable**\n⭐ Rating: {rate}%\n---\n📈 Entry: {entry}\n🎯 TP: {tp}\n❌ SL: {sl}\n⚖️ Lot: {lot}"
        bot.reply_to(message, msg, parse_mode='Markdown')

bot.polling()
