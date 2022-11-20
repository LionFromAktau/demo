a = []
for i in range(3):
    a.append(int(input()))
for i in range(2):
    for j in range(i + 1, 3):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(*a, sep=", ")