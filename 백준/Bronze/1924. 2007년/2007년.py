a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())
day = 0
for i in range(0, x - 1) :
  day += b[i]

result = (day + y) % 7

print(a[result])