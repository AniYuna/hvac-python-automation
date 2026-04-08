# Создание DataFrame с использованием нескольких Series с параметрами воздуховодов и базовой фильтрацией
import pandas as pd
# Создаем несколько Series
room = pd.Series(['Bedroom_1', 'Kitchen', 'Living_room', 'Bath_room', 'Corridor'])
air = pd.Series([150, 300, 250, 100, 80])
diameter = pd.Series([160, 250, 200, 125, 100])
status = pd.Series(['designed', 'ready', 'under testing', 'designed', 'ready'])
# Создаем из каждого Series один DataFrame
room_df = room.to_frame(name='Room_name')
air_df = air.to_frame(name='Air_flow_m3/h')
diameter_df = diameter.to_frame(name='Diameter_mm')
status_df = status.to_frame(name='Status')
# Объединяем их в один общий DataFrame, выстраиваем строки по горизонтали
df_systems = pd.concat([room_df, air_df, diameter_df, status_df], axis=1)
print("\n--- Ventilation systems data ---")
print(df_systems)
print("\n--- Ventilation velocities data ---")
# Расчет скорости в воздуховодах: V = L / (3600 * S)
import math
area = (math.pi * ((diameter / 1000) ** 2)) / 4
velocities = air / (3600 * area)
report = pd.DataFrame({
    'Room_name': room,
    'Diameter_mm': diameter,
    'Air_flow_m3/h': air,
    'Velocity_m/s': velocities
})
print(report.round(2)) # Округляем значение скорости до 2 знаков после запятой
# Прием с двойными скобками: выбираем только нужные колонки сразу как таблицу
final_table = report[['Room_name', 'Velocity_m/s']] 
# Переименуем колонку для краткости перед сохранением в файл (CSV)
final_table = final_table.rename(columns={'Velocity_m/s': 'V_m/s'})
# Сохраняем результат в файл Excel-формата (CSV)
final_table.to_csv('vent_velocity_report.csv', index=False)
print("Report saved successfully!")