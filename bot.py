import time
import requests

# List of URLs to keep alive
URLS = [
    "https://customer-churn-prediction-mkdr.onrender.com/",
    "https://your-second-app.onrender.com/",
    "https://your-third-app.onrender.com/",
]

INTERVAL = 250


def ping_urls():
    for url in URLS:
        try:
            response = requests.get(url, timeout=15)
            print(f"[{time.ctime()}]  {url} -> {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{time.ctime()}]  {url} -> {e}")


def keep_alive():
    print("Keep-Alive Bot Started...")
    
    while True:
        ping_urls()
        print("-" * 60)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    keep_alive()
