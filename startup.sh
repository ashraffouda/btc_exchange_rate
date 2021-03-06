sleep 10 # Postgres sql docker doing restart in its startup script as an initialization step so sleep 10 seconds
/etc/init.d/cron start
python manage.py migrate
python manage.py createsuperuser --noinput
# python manage.py crontab add

/etc/init.d/cron start
service redis-server start
celery -A btc_exchange_rate worker -l info &
celery -A btc_exchange_rate beat -l info &
python manage.py runserver 0.0.0.0:8000