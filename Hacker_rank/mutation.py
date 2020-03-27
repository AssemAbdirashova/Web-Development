s1 = input()
s2 = input().split()
s1 = s1[:int(s2[0])] + s2[1] + s1[int(s2[0]) + 1:]
print(s1)