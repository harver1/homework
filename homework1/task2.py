'''Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.'''



second = int(input("Введите количество секунд: >"))
sec = 1
minuta = sec * 60  # =>60
hour = minuta * minuta  # =>3600
day = hour * 24  # =>86400

days = second // day
hours = second % day // hour
minutes = second % day % hour // minuta
seconds = second % day % hour % minuta

print(f'{hours:02}:{minutes:02}:{seconds:02}')  #  форматирование через f строки
print('количество дней - {} \nвремя - {:02}:{:02}:{:02}'.format(days, hours, minutes, seconds))  #  форматирование с помощью метода format()