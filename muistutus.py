import schedule
import time
import requests

TOKEN = "8728949477:AAGcvw3elpbJODZLpBe7c9nLyJYz9envkk0"
CHAT_ID = "6227628456"

def laheta(viesti):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": viesti}
    )

def aamumuistutus():
    laheta("Punnitukseen boi alle 70kg pitäs olla")

schedule.every().day.at("07:05").do(aamumuistutus)

print("Muistutusohjelma käynnissä...")
while True:
    schedule.run_pending()
    time.sleep(30)
