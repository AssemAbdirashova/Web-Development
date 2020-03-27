x = int(input())
arr = list(map(int, input().split()))
for i in range(0, x):
    if i % 2 == 0:
      print(arr[i], end = ' ')