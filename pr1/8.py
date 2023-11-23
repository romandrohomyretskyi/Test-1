number = 5

array_size = 10 + number

my_array = []

for i in range(array_size):
    element = int(input(f"Введіть {i+1}-й елемент масиву: "))
    my_array.append(element)

max_element = max(my_array)

reversed_array = my_array[::-1]

print("Масив у зворотньому порядку:", reversed_array)
print("Максимальний елемент масиву:", max_element)