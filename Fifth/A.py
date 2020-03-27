def min(a, b, c, d):
    min = 0
    if(a > b): min = b
    else: min = a
    if(min > c): min = c
    if(min > d): min = d
    return min

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a,b,c,d))