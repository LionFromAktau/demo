a = []
for i in range(4):
    a.append(int(input()))
if a[0] != a[2] and a[1] == a[3]:
    print('YES')
elif a[0] == a[2] and a[1] != a[3]:
    print('YES')
else:
    print('NO')