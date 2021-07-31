import requests
import datetime
from .models import ExchangeEntry
import os

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")


def get_realtime_exchange_rate():
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    resp = requests.get(url)
    data = resp.json()
    rate = data.get("Realtime Currency Exchange Rate", {}).get("5. Exchange Rate")
    time = data.get("Realtime Currency Exchange Rate", {}).get("6. Last Refreshed")
    if not rate:  # something wrong happend return
        return
    if not time:
        time = datetime.datetime.now()
    else:
        time = datetime.datetime.fromisoformat(time)
    ex_entry = ExchangeEntry.objects.create(rate=rate, time=time)
    ex_entry.save()
    return ex_entry