a = []
for i in range(3):
    a.append(int(input()))
max = 0
for i in range (3):
    if a[i] > max:
        max = a[i]
print(max)