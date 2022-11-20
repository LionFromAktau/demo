a = int(input())
shortBreak = a // 2
longBreak = a - shortBreak - 1
result = int(shortBreak * 5 + longBreak * 15 + 45 * a)
hours = 9 + int(result / 60)
minutes = result % 60
print(f'{hours} {minutes}')