from prettyconf import Configuration

config = Configuration()

broker_url = config('BROKER_URL')
print(broker_url)

result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Sao_Paulo'
enable_utc = True
