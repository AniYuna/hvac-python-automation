import pandas as pd

# 1. Загружаем данные по сауне
df = pd.read_csv('sauna_airflow.csv')

# 2. Считаем баланс только для комнаты отдыха
rest_room_data = df.loc[df['Room'] == 'Rest_room']
supply = rest_room_data.loc[rest_room_data['Type'] == 'Supply', 'Flow_m3h'].sum()
extract = rest_room_data.loc[rest_room_data['Type'] == 'Extract', 'Flow_m3h'].sum()

balance = supply - extract

print("--- SAUNA AIRFLOW BALANCE REPORT ---")
print(df)
print(f"\nRoom: Rest_room")
print(f"Supply airflow:  {supply} m3/h")
print(f"Extract airflow: {extract} m3/h")
print(f"Balance in the break room: {balance} m3/h")

if balance > 0:
    print("\nResult: POSITIVE PRESSURE (Aii right for a recreation area)")
else:
    print("\nResult: NEGATIVE PRESSURE (check settings!)")