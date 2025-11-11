import time
import requests

URL = "https://customer-churn-prediction-mkdr.onrender.com/"

INTERVAL = 300  

def keep_alive():
    while True:
        try:
            response = requests.get(URL)
            print(f"[{time.ctime()}] Pinged {URL} → Status: {response.status_code}")
        except Exception as e:
            print(f"[{time.ctime()}] Error pinging site: {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    print("🟢 Keep-Alive bot started...")
    keep_alive()
else:
    print("Bot Not working");