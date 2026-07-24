import requests

URLS = [
    "https://customer-churn-prediction-mkdr.onrender.com/",
    # Add more URLs here
    "https://synapse-the-learning-platform-mnk9.onrender.com/",
]

for url in URLS:
    try:
        response = requests.get(url, timeout=20)
        print(f" {url} -> {response.status_code}")
    except Exception as e:
        print(f" {url} -> {e}")
