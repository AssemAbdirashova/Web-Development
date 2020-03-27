list = []
for i in range(int(input())):
    s = input().split()
    for i in range(1, len(s)):
        s[i] = int(s[i])
    if(s[0] == 'insert'):
        list.insert(s[1], s[2])
    if(s[0] == 'print'):
        print(list)
    if(s[0] == 'remove'):
        list.remove(s[1])
    if(s[0] == 'append'):
        list.append(s[1])
    if(s[0] == 'sort'):
        list.sort()
    if(s[0] == 'pop'):
        list.pop()
    if(s[0] == 'reverse'):
        list.reverse()