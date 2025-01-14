import numpy as np
import sys
import array
x=1 #000000000000000000000000000000000
print(type(x))
print(sys.getsizeof(x))

#x='hello'
#print(type(x))

#x=True
#print(type(x))

# l1=list([])
# print(sys.getsizeof(l1))

# l2=list([1,2,3])
# print(sys.getsizeof(l2))

# l3=list([1,"2",True])
# print(sys.getsizeof(l3))

# a1=array.array('i',[1,2,3])
# print(sys.getsizeof(a1))
# print(type(a1))

# a=np.array([1,2,3,4,5])
# print(type(a),a)

# #"повышающее приведение типов"
# a=np.array([1.23,2,3,4,5])
# print(type(a),a)

# a=np.array ([1.23,2,3,4,5], dtype=int) #округление
# print(type(a),a)

# a =np.array([range(i,i+3) for i in [2,4,6]])
# print(a, type(a[1]))

# a=np.zeros(10,dtype=int)
# print(a, type(a[1]))

# print(np.ones((3,5), dtype=float))

# print(np.full((3,5), 3.333))

# print(np.arange(0,21,1))

# print (np.eye(4))


np.random.seed(1)

# x1=np.random.randint(10,size=3)
# x2=np.random.randint(10,size=(2,3))
# x3=np.random.randint(10,size=(2,3,4))

# print(x2)

# print(x1.ndim, x1.shape, x1.size)
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

# a=np.array([1,2,3,4,5])
# print(a[-2])

# a[1]=20
# print(a)

# a=np.array([[1,2],[3,4]])
# print(a[0,0])

# a[1,0]=100
# print(a)

# a=np.array([1,2,3,4])
# b=np.array([1.0,2,3,4])

# print(a)
# print(b)

# a[0]=10
# print(a)

# a[0]=10.122
# print(a)

# срез [нач:кон:шаг]

# a=np.array([1,2,3,4,5,6])

# print(a[:3]) # до 3-го
# print(a[3:])
# print(a[1:-1])
# print(a[1::2])
# print(a[:6:2])

# print(a[::-1])# меняет старт и финиш
# #[кон:нач:шаг]

# #срез=ссылка
# a=np.array([1,2,3,4,5,6])

# b=a[:3]
# b[0]=100
# print(a)

# a=np.arange(1,13)

# print(a.reshape(2,6))
# print(a.reshape(3,4))

# x=np.array([1,2,3])
# y=np.array([4,5])
# z=np.array([6])

# print(np.concatenate([x,y,z]))

# x=np.array([1,2,3])
# y=np.array([4,5,6])

# r1=np.vstack([x,y])
# print(r1)

# print(np.dstack([r1,r1]))

# вычисления с массивами
# векторезированая опер.=к каждому

# x=np.arange(10)
# print(x)

# print(x*2+1)


# print(np.add(np.multiply(x,2),1))
# #         ^         ^
# #         |         |
# универсальные ф-ии - ф-ии ...

# - -1 / // ** %

#бонус  np.abs, sin/cos/tan (-1), exp, log
 
x=np.arange(5)

#y=np.array([0,0,0,0,0,0,0,0,0,0])
# y=np.zeros(10)
# print(y)
# print(np.multiply(x,10, out=y[::2]))
# print(y)

# x= np.arange(1,5)

# print(x)
# print(np.add.accumulate(x))

x=np.arange(1,10)
print(np.multiply.outer(x,x))