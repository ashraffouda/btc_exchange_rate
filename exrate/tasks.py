from btc_exchange_rate.celery import app

from .helpers import get_realtime_exchange_rate



@app.task
def get_realtime_exchange():
    get_realtime_exchange_rate()
