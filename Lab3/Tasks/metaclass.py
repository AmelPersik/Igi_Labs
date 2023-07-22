from types import FunctionType

#change methods yo lowercase
class Meta(type):
    def __new__(cls, name, base, attrs):
        new_attrs = dict()
        for k,v in attrs.items():
            if isinstance(v, FunctionType):
                if k[0] =='_' and k[1] == '_':
                    new_attrs[k] = v
                else:
                    k=k.lower()
                    new_attrs[k]=v
        return super().__new__(cls, name, base, new_attrs)
class A(metaclass = Meta):
    def __init__(self):
        pass
    def ABC(self):
        pass

print(dir(A()))

#change name of the class to lower
class Meta(type):
    def __new__(cls, name, base, attrs):
        new_name = name.lower()
        return super().__new__(cls, new_name, base, attrs)

class BIGCLASS(metaclass=Meta):
    pass

a = BIGCLASS()
print(a.__class__.__name__)

#check attrs in class
class IntMeta(type):
    def __new__(cls, name, bases, attrs):
        int_attrs = {key : value for key, value in attrs.items() if isinstance(value, int)}
        return super().__new__(cls, name, bases, int_attrs)

class MyClass(metaclass=IntMeta):
    x = 10
    y = "str"

print(hasattr(MyClass, "x"))
print(hasattr(MyClass, "y"))

#change mro

class A:
    @staticmethod
    def meth():
        print('20')

class B:
    @staticmethod
    def meth():
        print('9')

class G:
    @staticmethod
    def meth():
        print("40")

class MroMeta(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls,name,bases[::-1],attrs)

class V(A,B,G,metaclass=MroMeta):
    pass

V.meth()