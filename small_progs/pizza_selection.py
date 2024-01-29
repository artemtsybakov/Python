# "Что лучше? Одна большая или 2 одинаковых маленьких?". Программа считает
# площадь пицы через диаметр и помогает принять решение.
# Ввод диаметра пиццы. 
diameter_small_pizza = float(input('Введите диаметр двух маленьких пицц: '))
width_skirting_small_pizza = float(input('-Введите ширину бортика: '))
diameter_big_pizza = float(input('Введите диаметр одной большой пиццы: '))
width_skirting_big_pizza = float(input('-Введите ширину бортика: '))
p = 3.1415926

# Получение площади через диаметр пиццы.
small_two_pizza_space = ((p*diameter_small_pizza**2)/4)*2
big_pizza_space = (p*diameter_big_pizza**2)/4

# Вывод диаметров.
print('Диаметр двух маленьких пицц: ', small_two_pizza_space)
print('Диаметр одной большой пиццы:', big_pizza_space)

# Получение площади без бортиков.
diameter_small_pizza = diameter_small_pizza - width_skirting_small_pizza
diameter_big_pizza = diameter_big_pizza - width_skirting_big_pizza
small_two_pizza_space = ((p*diameter_small_pizza**2)/4)*2
big_pizza_space = (p*diameter_big_pizza**2)/4
print('Диаметр двух маленьких пицц без бортиков: ', small_two_pizza_space)
print('Диаметр одной большой пиццы без бортиков:', big_pizza_space)
