a, b, c, d = map(int,input().split())

abc = (a + b + c)
abd = (a + b + d)
acd = (a + c + d)
bcd = (b + c + d)

if a >= bcd or b >= acd or c >= abd or d >= abc:
    print('S')
else:
    print('N')
