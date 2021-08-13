from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btc_exchange_rate.settings')

app = Celery('btc_exchange_rate')
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Cairo')
app.config_from_object(settings, namespace="CELERY")

#celery beat 
app.autodiscover_tasks()
