x = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in range(0, x):
    if(arr[i] > 0):
        cnt += 1
print(cnt)