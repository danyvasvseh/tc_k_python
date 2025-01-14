import numpy as np
import array
import sys
# 1. Какие еще существуют коды типов?

#    - 'b' - signed char (целое со знаком) 
#    - 'B' - unsigned char (целое без знака)
#    - 'u' - Unicode character (старая строка юникода)
#    - 'w' - Unicode character (новая строка юникода)
#    - 'h' - signed short (короткое целое со знаком)
#    - 'H' - unsigned short (короткое целое без знака)
#    - 'i' - signed int (целое со знаком)
#    - 'I' - unsigned int (целое без знака)
#    - 'l' - signed long (длинное целое со знаком)
#    - 'L' - unsigned long (длинное целое без знака)
#    - 'q' - signed long long (очень длинное целое со знаком)
#    - 'Q' - unsigned long long (очень длинное целое без знака)
#    - 'f' - float  с плавающей запятой)
#    - 'd' - double (двойная точность, с плавающей запятой)

# 2. Напишите код с другим типом
a1=array.array('I',[1,2,3])
#print(sys.getsizeof(a1))
#print(type(a1))

# 3. Напишите код для создания массива с 5 значениями,
#  располагающимися через равные интервалы в диапазоне от 0 до 1
a = np.linspace(0, 1, 5)
#print(a)

# 4. Напишите код для создания массива с 5 равномерно
#  распределенными случайными значениями в диапазоне от 0 до 1
a = np.random.uniform(0, 1, 5)
#print(a)

# 5. Напишите код для создания массива с 5 
# нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1
a = np.random.normal(0, 1, 5)
#print(a)

# 6. Напишите код для создания массива с 5
#  случайнвми целыми числами в от [0, 10)
a = np.random.randint(0, 10, 5)
#print(a)

# 7. Написать код для создания срезов массива 3 на 4
a = np.array([[1, 2,  3,  4],
              [5, 6,  7,  8],
              [9, 10, 11, 12]])

# - первые две строки и три столбца
b = a[:2, :3]
#print(b)
# - первые три строки и второй столбец
c = a[:3, 1:2]
#print(c)
# - все строки и столбцы в обратном порядке
d = a[::-1, ::-1]
#print(d)
# - второй столбец
e = a[:, 1]
#print(e)
# - третья строка
f = a[2, :]
#print(f)

# 8. Продемонстрируйте, как сделать срез-копию
b = np.copy(b)
b[1][0]=1111
# print(a)
# print(b)

# 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки
a = np.array([1, 2, 3, 4, 5])
#print(a)

column = a[:, np.newaxis]
#print(column)

row = a[np.newaxis]
#print(row)

# 10. Как работает метод dstack

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.dstack((a, b))
#print(c)

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.dstack((a, b))
#print(c) # поставили массивы в стопку и проткнули насквозь

#11. Как работают методы split, vsplit, hsplit, dsplit
# - split
a = np.array([[[1], [2], [3]], [[4],[ 5], [6]], [[7], [8], [9]]])
b = np.split(a, 3, 0)
c = np.split(a, 3, 1)
d = np.split(a, 1, 2)
print(b,c,d)
# vsplit = split( , , 0), hsplit = split( , , 1), dsplit = split( , , 2)

# 12. Привести пример использования всех универсальных функций, которые были приведены

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

# 12. Арифметические операции
print( np.add(x, y))      # Сложение
print( np.subtract(x, y)) # Вычитание
print( np.multiply(x, y)) # умножение
print( np.divide(y, x))   # Деление
print( np.negative(x))    # Унарный минус
print( np.floor_divide(x,y)) #Деление с округлением
print( np.power(x,y))    # Степень
print( np.mod(x,y))      # Остаток от деления
# технически, они приводились
print( np.sin(x))        # Синус
print( np.cos(x))        # Косинус
print( np.tan(x))        # Тангенс:
print( np.arcsin(x))     # Арксинус
print( np.arccos(x))     # Аркосинус
print( np.arctan(x))     # Арктангенс:
print( np.exp(x))        # Натуральный логарифм
print( np.log(x))        # Экспонента
