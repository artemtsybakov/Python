name1 = 'Mary'
name2 = 'Mary'
if name1 == name2:
    print('Имена одинаковые')
else:
    print('Имена разные')

if 'a' < 'б':
    print('Буква а < b.')

name1 = 'Mary'
name2 = 'Mark'
if name1 > name2:
    print('Строка Mary больше строки Mark')
else:
    print('Строка Mark больше строки Mary')

s1 = 'Нью-Йорк'
s2 = 'Бостон'
if s1 > s2:
    print(s2)
    print(s1)
else:
    print(s1)
    print(s2)

number = int(input('Введите число: '))
if number == 1:
    print('Один')
else:
    if number == 2:
        print('Два')
    else:
        if number == 3:
            print('Три')
        else:
            print('Неизвестное')
#
print('Через if-elif-else')
if number == 1:
    print('Один')
elif number == 2:
    print('Два')
elif number == 3:
    print('Три')
else:
    print('Неизвестное')
    
