from Task1 import print_hello_world
from Task2 import basic_calculations
from Task3 import even_list

print("Task1: " + print_hello_world())

print("\nTask2: ")
print(basic_calculations(6, 7, "add"))
print(basic_calculations(1, 2, "mul"))
print(basic_calculations(8, 5, "sub"))
print(basic_calculations(1, 0, "div"))
print(basic_calculations(1, 0, "way"))

print("\nTask3:")
print(even_list([num for num in range(1, 50)]))
