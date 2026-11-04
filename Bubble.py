n = int(input("Enter the number of elements: "))

a = []

print("Enter the elements:")
for i in range(n):
    number = int(input())
    a.append(number)


    # Bubble Sort
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted elements:" , a)
