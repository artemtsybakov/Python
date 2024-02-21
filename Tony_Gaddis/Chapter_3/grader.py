# Эта программа получает от пользователя количетво баллов
# и показывает соответствующий буквенный уровень знаний.

# Именованные константы, представляющие пороги уровней.
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Получить от пользоватеял баллы за котрольную рабоу.
score = int(input('Введите свои баллы: '))

# Определить буквенный уровень.
if score >= A_SCORE:
    print('Ваш уровень - A.')
else:
    if score >= B_SCORE:
        print('Ваш уровень - B.')
    else:
        if score >= C_SCORE:
            print('Ваш уровень - C.')
        else:
            if score >= D_SCORE:
                print('Ваш уровень - D.')
            else:
                print('Ваш уровень - F.')
        
# Второй вариант с if-elif-else
print('Второй вариант с if-elif-else')
if score >= A_SCORE:
    print('Ваш уровень - A.')
elif score >= B_SCORE:
    print('Ваш уровень - B.')
elif score >= C_SCORE:
    print('Ваш уровень - C.') 
elif score >= D_SCORE:
    print('Ваш уровень - D.')
else:
    print('Ваш уровень - F.')
