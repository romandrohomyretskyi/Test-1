student_number = 5

M = 10

X = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]  

Y = [x for x in X if abs(x) > M]

print("Число M:", M)
print("Масив X:", X)
print("Масив Y:", Y)