import logging

worker_class = 'gevent'
worker_connections = 25
workers = 4
bind = 'unix:///tmp/nginx.socket'


def when_ready(server):
    open('/tmp/app-initialized', 'w').close()


def pre_fork(server, worker):
    import gevent.monkey
    import psycogreen.gevent
    gevent.monkey.patch_all()
    logging.info('Making code green')
    psycogreen.gevent.patch_psycopg()
    logging.info('Making postgres green')
