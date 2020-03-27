a = int(input())
i = 0
while 2 ** i <= a:
    if 2 ** i == a: even = True
    else: even = False
    i = i + 1
if(even): print('YES')
else:print('NO')