release:  python manage.py migrate
web: bin/start-nginx bin/start-pgbouncer gunicorn -w $WORKERS -c gunicorn_config.py config.wsgi:application



