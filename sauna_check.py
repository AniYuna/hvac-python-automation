import pandas as pd

# 1. Загружаем данные по сауне
df = pd.read_csv('sauna_airflow.csv')

# 2. Считаем баланс только для комнаты отдыха
rest_room_data = df.loc[df['Room'] == 'Rest_room']
supply = rest_room_data.loc[rest_room_data['Type'] == 'Supply', 'Flow_m3h'].sum()
extract = rest_room_data.loc[rest_room_data['Type'] == 'Extract', 'Flow_m3h'].sum()

balance = supply - extract

print("--- АНАЛИЗ ВОЗДУХООБМЕНА САУНЫ ---")
print(df)
print(f"\nБаланс в комнате отдыха: {balance} м3/ч")

if balance > 0:
    print("Результат: Подпор (все отлично для чистой зоны)")
else:
    print("Результат: Разрежение (проверьте настройки!)")