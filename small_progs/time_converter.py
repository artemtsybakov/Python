# Получить от пользователя количество секунд.
total_seconds = int(input('Введите количество секунд: '))

# Получить количесвто часов.
hours = total_seconds // 3600

# Получить количество оставшихся минут.
minutes = (total_seconds // 60) % 60

# Получить количество оставшихся секунд.
seconds = total_seconds % 60

# Показать результаты
print('Вот время в часах, минутах и секундах: ')
print('Часы: ', hours)
print('Минуты: ', minutes)
print('Секунды: ', seconds)
print(hours,':', minutes,':',seconds)
