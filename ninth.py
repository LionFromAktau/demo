a = []
for i in range(3):
    a.append(int(input()))
count = 0
for i in range(2):
    for j in range(i + 1, 3):
        if a[i] == a[j]:
            count += 1
print( 2 if count == 1 else count )