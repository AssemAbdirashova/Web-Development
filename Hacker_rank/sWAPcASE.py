s = input()
cur = ""
for i in s:
    if i.isupper() == True:
        cur += i.lower()
    else:
        cur += i.upper()
print(cur)