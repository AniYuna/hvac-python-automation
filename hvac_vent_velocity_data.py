# Создание DataFrame с использованием нескольких Series с параметрами воздуховодов и базовой фильтрацией
import pandas as pd
import numpy as np
# Создаем несколько Series
room = pd.Series(['Bedroom_1', 'Kitchen', 'Living_room', 'Bath_room', 'Corridor'])
air = pd.Series([150, 300, 250, 100, 80])
diameter = pd.Series([160, 250, 200, 125, 100])
status = pd.Series(['designed', 'ready', 'under testing', 'designed', 'ready'])
# Создаем из каждого Series один DataFrame
df_systems = pd.DataFrame({
    'Room_name': room,
    'Air_flow_m3/h': air,
    'Diameter_mm': diameter,
    'Status': status
})
print("\n--- Ventilation velocities data ---")
# Расчет скорости в воздуховодах: V = L / (3600 * S)
df_systems['Area_m2'] = ((np.pi * (df_systems['Diameter_mm'] / 1000) ** 2) / 4)
df_systems['Velocity_m/s'] = df_systems['Air_flow_m3/h'] / (3600 * df_systems['Area_m2'])
df_systems['Status_velocity'] = df_systems['Velocity_m/s'].apply(
    lambda x: 'OK' if 2 <= x <= 5 else 'Check'
)
print(df_systems.round(3)) # Округляем значение скорости до 3 знаков после запятой
# Переименуем колонку для краткости перед сохранением в файл (CSV)
final_table = df_systems[['Room_name', 'Velocity_m/s', 'Status_velocity']].rename(columns={'Velocity_m/s': 'V_m/s'})
# Сохраняем результат в файл Excel-формата (CSV)
final_table.to_csv('vent_velocity_report.csv', index=False)
print("Report saved successfully!")