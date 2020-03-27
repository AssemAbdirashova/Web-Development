def xor(x, y):
    if(x != y): return 1
    if(x == y): return 0

a = int(input())
b = int(input())
if (a == 0 or a == 1) and (b == 0 or b == 1): print(xor(a, b))
else: print('Please enter correct values!')