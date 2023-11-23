number = 5

a = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]  

for i in range(len(a)):
    if a[i] < 0:
        a[i] = abs(a[i])

print("Масив:", a)