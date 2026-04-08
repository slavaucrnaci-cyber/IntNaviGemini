import os
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes — только чтение активности и пульса
SCOPES = [
    'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/fitness.heart_rate.read'
]

# Путь к credentials.json
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

creds = None

# Если уже есть токен, используем его
if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

# Если токена нет или он просрочен
if not creds or not creds.valid:
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    # Сохраняем токен для повторного использования
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())

# Создаём сервис Fitness API
service = build('fitness', 'v1', credentials=creds)

# Пробуем получить последние данные активности (за сегодня)
end_time = int(datetime.datetime.utcnow().timestamp() * 1000)
start_time = end_time - 24*60*60*1000  # 24 часа назад

dataset = f"{start_time}-{end_time}"

# Пример: чтение шагов
data_source_id = "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"

try:
    steps = service.users().dataSources().datasets().get(
        userId='me',
        dataSourceId=data_source_id,
        datasetId=dataset
    ).execute()
    
    print("Данные шагов за последние 24 часа:")
    if 'point' in steps:
        for point in steps['point']:
            start = int(point['startTimeNanos']) / 1e9
            end = int(point['endTimeNanos']) / 1e9
            value = point['value'][0]['intVal']
            print(f"{datetime.datetime.fromtimestamp(start)} - {datetime.datetime.fromtimestamp(end)} : {value} шагов")
    else:
        print("Нет данных за выбранный период.")
except Exception as e:
    print("Ошибка при чтении данных:", e)