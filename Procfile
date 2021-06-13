release:  python manage.py migrate
web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program bin/start-nginx bin/start-pgbouncer gunicorn -w $WORKERS -c gunicorn_config.py config.wsgi:application



