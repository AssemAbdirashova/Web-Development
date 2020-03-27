n = int(input())
list = map(int, input().split())
t = tuple(list)
print(hash(t))