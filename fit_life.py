# Проект FitLife - MVP версия 1.0
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 1. Знакомство
print('Приветствуем вас в программе FitLive')
user_name = input('Введите ваше имя :')
user_name = user_name.title()
user_age = int(input('Укажите ваш возраст:'))

# 2. Сбор данных
user_weight = float(input('Укажите ваш вес (в кг.):'))
user_height = float(input('укажите ваш рост (в метрах, например 1.75):'))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = round((user_weight / user_height ** 2), 1)
water_needed = (user_weight * 30)/1000

# 4. Вывод красивого результата
print(f'Привет {user_name}! {user_age} г.' ) 
print(f'индекс массы тела: {bmi}') 
print (f'необходимое колличество воды в сутки: {water_needed} л.')
print("Расчет окончен. Будьте здоровы!")