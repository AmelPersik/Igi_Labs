import math
from src.factory import Factory
from src.constants import JSON_DATA_TYPE, XML_DATA_TYPE
#import src.supportive as sup

from src.converter import Converter

serializer = Factory.create_serializer(JSON_DATA_TYPE)

def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner

class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = Factory.create_serializer(XML_DATA_TYPE)
#
#var = 15
#var_ser = ser.dumps(var)
#var_des = ser.loads(var_ser)
#print(var_des)
#
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

#conv = Converter()

c = C_des(1, 2)


#c_conv = conv.convert(c)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

#print(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))

print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())

listt = [12,23,34]

x = (x for x in listt)
#print(x)
c_ser = ser.dumps(x)
c_des = ser.loads(c_ser)


def gx():
    for i in [1,2,3]:
        yield i
def gy():
    for i in [11,12,13]:
        yield i

def gz():
    yield from gx()
    yield from gy()

gz = gz()

c_ser = ser.dumps(gz)
d_ser = ser.loads(c_ser)


for _ in range(6):
    print(next(d_ser))



# l = lambda x:x**2
# c_ser = ser.dumps(l)
# c_des = ser.loads(c_ser)
#
# print(c_des(5))
#
#
# sum = 5
# def recurce(sum):
#     while (sum !=0):
#         sum-=1
#         print(sum)
#         return recurce(sum)
#
# c_ser = ser.dumps(recurce)
# c_des = ser.loads(c_ser)
# c_des(5)



def my_func(*args, **kwargs):

    newkwargs = []
    for key, val in enumerate(kwargs):
        newkwargs.append(kwargs[val])

    return sum(newkwargs) + sum(args)

print(my_func(12,23,43, a=4))

#filter(func, list)



list = list(filter(lambda x:x%2, [1,2,3]))

print(list)


def func(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(func(1,2,3,4,a=2, b=7))


# class MyClass:
#     def __init__(self, num):
#         self.num = num
#
#     def __hash__(self):
#         raise TypeError("should not be hashed")
#
# obj = MyClass(42)
#
# my_set = set()
#
# try:
#     my_set.add(obj)
# except TypeError as e:
#     print(f"Mistake: {e}")















# list = [12,34,"str", {12,23}]
#
# def checkhash(list):
#     newlist = []
#     for i in list :
#         try:
#             hash(i)
#             newlist.append(i)
#         except:
#             pass
#     return newlist
#
# list = checkhash(list)
# set = {x for x in list}
# print(set)

#
# class A:
#     @staticmethod
#     def meth():
#         print('20')
#
# class B:
#     @staticmethod
#     def meth():
#         print('9')
#
# class G:
#     @staticmethod
#     def meth():
#         print("40")
#
# class AttrMeta(type):
#     pass
#
# class MyClass(metaclass=AttrMeta):
#     x = 20
#     y = "str"
#
# a = MyClass()
#
# print(hasattr(MyClass, "x"))
# print(hasattr(MyClass, "y"))
#
# from types import FunctionType
# class Meta(type):
#     pass
#
#
# class A(metaclass = Meta):
#     def __init__(self):
#         pass
#     def abc(self):
#         pass
#
# print(dir(A()))
#
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
#
# fib = fib()
#
# for _ in range(10):
#     print(next(fib))


# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         return super().__new__(cls, name, bases, attrs)
# class A(metaclass=Meta):
#     @staticmethod
#     def pr():
#         print("Hello meta")
#
# x = A()
#
# c_ser = ser.dumps(x.pr())
# #c_des = ser.loads(c_ser)


'''

class MyClass():
    x = 20
    y = "str"

print(hasattr(MyClass, "x"))
print(hasattr(MyClass,"y"))



class PowerIter:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        

pi = PowerIter(4)
for it in pi:
    print (it)


class MyContextManager:
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is ZeroDivisionError:
            print("devision by zero")
        return True

with MyContextManager():
    result = 1/0

def fib(n):
    a,b=1,1
    for i in range(n):
        a, b = b, a + b
        i += 1
        yield a


ser_fib = ser.dumps(fib(10))
des_fib = ser.loads(ser_fib)

for it in des_fib:
    print(it)



liiist = [4,5,6,(True, 45, 'dfdfdf', {'set1', 'set2','set3'})]
print(conv.convert(liiist))
print(serializer.dumps(liiist))
print(ser.dumps(liiist))


sum = 10
def rec_func(sum):
    while(sum!=0):
        sum-= 1
        print(sum)
        return rec_func(sum)

lost = lambda x:x**2
print(serializer.dumps(lost))
print(ser.dumps(lost))

def decor_func(func):
    def sum(a,b):
        return a+b
    return sum

@decor_func
def mul(a,b):
    return a*b

print(mul(12,4))

class MyContextManager():
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        if (exc_type == ZeroDivisionError):
            return True

with MyContextManager():
    1/0
'''