a = int(input())
b = int(input())
c = int(input())
d = int(input())

diferenca = 10**4

if (a + b) > (c + d):
    if (((a + b))-((c + d))) < diferenca:
        diferenca = ((a + b))-((c + d))

if (a + b) < (c + d):
    if (((c + d))-((a + b))) < diferenca:
        diferenca = ((c + d))-((a + b))

if (a + c) > (b + d):
    if (((a + c))-((b + d))) < diferenca:
        diferenca = ((a + c))-((b + d))

if (a + c) < (b + d):
    if (((b + d))-((a + c))) < diferenca:
        diferenca = ((b + d))-((a + c))

if (a + d) > (b + c):
    if (((a + d))-((b + c))) < diferenca:
        diferenca = ((a + d))-((b + c))

if (a + d) < (b + c):
    if (((b + c))-((a + d))) < diferenca:
        diferenca = ((b + c))-((a + d))

if (a + b) == (c + d) or (a + c) == (b + d) or (a + d) == (b + c):
    print(0)
else:
    print(diferenca)