import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series

# - списки Python или массивы NumPy
# Из списка Python
list = [1, 2, 3, 4, 5]
slist = pd.Series(list)
print(slist)

# Из массива NumPy
array = np.array([10, 20, 30, 40])
sarr = pd.Series(array)
print(sarr)

# - скалярные значение
a = 7
sscal = pd.Series(a, index=[0, 1, 2, 3])  
print(sscal)

# - словари
dict = {'a': 1, 'b': 2, 'c': 3}
sdict = pd.Series(dict)
print(sdict)

# 2. Привести различные способы создания объектов типа DataFrame
# - через объекты Series
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
df = pd.concat([s1, s2], axis=1)
print(df)

# - списки словарей
data = [
    {'A': 1, 'B': 4},
    {'A': 2, 'B': 5},
    {'A': 3, 'B': 6}
]
df = pd.DataFrame(data)
print(df)

# - словари объектов Series
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
data = {'A': s1, 'B': s2}
df = pd.DataFrame(data)
print(df)

# - двумерный массив NumPy
data = np.array([[1, 4], [2, 5], [3, 6]])
df = pd.DataFrame(data, columns=['A', 'B'])
print(df)

# - структурированный массив Numpy
data = np.array([(1, 4), (2, 5), (3, 6)],
                 dtype=[('A', 'i4'), ('B', 'i4')])
df = pd.DataFrame(data)
print(df)

# 3. Объедините два объекта Series с 
# неодинаковыми множествами ключей (индексов) так, 
# чтобы вместо NaN было установлено значение 1

s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2], index=['b', 'd'])

result = s1.combine_first(s2).fillna(1)
print(result)


# 4. Переписать пример с транслирование для DataFrame так, 
# чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng()
A = rng. integers (0, 10, (3,4))
df = pd.DataFrame (A, columns=['a', 'b', 'c', 'd'])

print(df)
print( )
print((df.T - df.iloc[:,0].T).T) # топорный
print( )
print(df.subtract(df.iloc[:,0], axis=0)) # замороченный

# 5. На примере объектов DataFrame
#  продемонстрируйте использование методов ffill() и bfill()
data = {
    'A': [None, 2, 3, 4, np.nan],
    'B': [np.nan, 2, 3, 4, pd.NA],
    'C': [pd.NA, 2, 3, 4, None]
}

df = pd.DataFrame(data)
print(df)

df_ffill = df.ffill()
print(df_ffill)

df_bfill = df.bfill()
print(df_bfill)
