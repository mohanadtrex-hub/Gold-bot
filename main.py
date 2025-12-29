import requests
import time

# بيانات Mohanad الأساسية
API_KEY = "pfBfuOpYRz/P9DYeXrGmCQ==ts6KbiuJvatvBSrY"
TOKEN = "8244331084:AAEFT5RyZFQtiWixKMIGPp1puczPXN-SpaE"
CHAT_ID = "8372781252"

# الرصيد اليدوي (تقدر تغيره في أي وقت من هنا)
BALANCE = 1200 

def get_gold_price():
    url = f'https://api.api-ninjas.com/v1/goldprice'
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['price']
    except:
        return None
    return None

def run_bot():
    print(f"Bot started for Mohanad. Initial Balance: {BALANCE}")
    while True:
        price = get_gold_price()
        if price:
            # نظام التقييم (Rating System) قبل التنبيه
            # إذا كان السوق غير مستقر يطبع:
            # print("time not appropriate")
            print(f"Current Gold Price: {price} - System Reviewing Conditions...")
        time.sleep(60)

if name == "__main__":
    run_bot()
