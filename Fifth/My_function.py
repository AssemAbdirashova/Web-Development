def max(a, b, c, d):
    max = 0
    if(a < b): max = b
    else: max = a
    if(max < c): max = c
    if(max < d): max = d
    return max

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(max(a,b,c,d))