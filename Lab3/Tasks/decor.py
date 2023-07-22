def decor_func(func):
    def sum(a,b):
        return a+b
    return sum

@decor_func
def mul(a,b):
    return a*b

print(mul(12,4))

def limit(n):
    def wrapper(func):
        def inner(*args, **kwargs):
            if len(args) + len(kwargs) > n:
                raise ValueError("too much arguments")
            return func(*args, **kwargs)
        return inner
    return wrapper

@limit(3)
def sum_func(*args):
    return sum(args)

print(sum_func(1, 2, 3))


def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print("значение уже вычислялось")
            return cached_results[args]

        else:
            result = func(*args)
            cached_results[args] = result
            return result
    return wrapper

@cache
def my_func(n):
    return n**2

print(my_func(2))
print(my_func(5))
print(my_func(2))

# Выводит на экран имя функции
def decorator(func):
	def wrapper(*args, **kwargs):
		print(f"Имя функции{func.__name__}")
		return func(*args, **kwargs)
	return wrapper

@decorator
def myFunc():
	pass

# Проверяет, что все аргументы функции являются числами
# def decorator(func):
#     def wrapper(*args):
# 		for arg in args:
# 			if not isinstance(arg, (int, float)):
# 				return func(*args)
#     return wrapper

@decorator
def myFunc():
    pass

# Кеширует результаты выполнения функции
# Если функция уже вызывалась с такими аргументами, то сейчас она уже не должна вызываться
def decorator(func):
	cached_results = {}

	def wrapper(*args):
		if args in cached_results:
			print ("уже вычислялось")
			return cached_results[args]

		else:
			result = func(*args)
			cached_results[args] = result
			return result

	return wrapper

@decorator
def myFunc():
	pass

# Проверяет количество аргументов, если больше 10, то он пишет
def decorator(func):
	def wrapper(*args):
		if len(args) > 10:
			print("more then 10")
			return func(*args)
		return wrapper

@decorator
def my_func(*args):
	pass



# Чисел Фибоначчи
def decorator(func):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = func(n)
			return cache[n]
		return wrapper

@decorator
def my_func(n):
	if n <= 1:
		return n

	return my_func(n-1) + my_func(n-2)

# Степени двойки
def decorator(func):
	def wrapper(n):
		result = 2 ** n
		return func(result)
	return wrapper

@decorator
def my_func(n):
	print(n)



# Если значение функции int, то добавить к нему какое-нибудь значение (+3)
def decorator(func):
	def wrapper(*args, n):
		if isinstance(args, n):
			return func(args + n)
		else:
			return func(args)

	return wrapper

@decorator
def my_func(args):
	return args