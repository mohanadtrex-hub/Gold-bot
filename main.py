import telebot
import datetime

# --- إعدادات البوت ---
# ملاحظة: تأكد من وضع التوكن كاملاً بين علامتي التنصيص
API_TOKEN = '7611986423:AAH_Ff6u6p7h9X4C9_wN3_qZ-mK4eR_xY'
BALANCE = 1200
PER_TRADE = 0.01

bot = telebot.TeleBot(API_TOKEN)

def get_market_rating():
    """
    هذه الدالة تقوم بمراجعة سريعة لظروف السوق.
    يمكنك لاحقاً ربطها بمؤشرات حقيقية (RSI, MACD).
    """
    # حالياً سنضع تقييم افتراضي
    rating = 85 
    return rating

def quick_review():
    """
    مراجعة نهائية قبل إرسال التنبيه
    """
    rating = get_market_rating()
    
    # إذا كان السوق غير مستقر (تقييم أقل من 75 مثلاً)
    if rating < 75:
        return False, "time not appropriate"
    
    return True, "Success"

@bot.message_handler(commands=['start', 'trade'])
def handle_trade_request(message):
    # القيام بالمراجعة السريعة قبل أي خطوة
    can_trade, status_message = quick_review()
    
    if not can_trade:
        # إذا الحالة غير مستقرة يرسل الرسالة التي طلبتها
        bot.reply_to(message, status_message)
    else:
        # إذا الأمور تمام يرسل التنبيه مع التقييم
        current_rating = get_market_rating()
        alert_msg = (f"🔔 **تنبيه صفقة جديدة**\n"
                     f"--- \n"
                     f"✅ حالة السوق: مستقرة\n"
                     f"📊 تقييم المؤشرات: {current_rating}/100\n"
                     f"💰 الرصيد المخصص: {BALANCE * PER_TRADE}")
        
        bot.reply_to(message, alert_msg)

# تشغيل البوت
print("Gold Bot is running...")
bot.infinity_polling()
