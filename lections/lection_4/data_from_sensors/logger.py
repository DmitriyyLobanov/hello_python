# модуль логирующий данные

from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('C:\\Users\\Zver\\Desktop\\GeekBrains\\python\\lections\\lection_4\\data_from_sensors\\log.csv', 'a') as file:
        file.write(f'{time};temperature;{data}\n')

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('C:\\Users\\Zver\\Desktop\\GeekBrains\\python\\lections\\lection_4\\data_from_sensors\\log.csv', 'a') as file:
        file.write(f'{time};pressure;{data}\n')

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('C:\\Users\\Zver\\Desktop\\GeekBrains\\python\\lections\\lection_4\\data_from_sensors\\log.csv', 'a') as file:
        file.write(f'{time};wind_speed;{data}\n')