a, b, c, d = map(int,input().split())
ab = a + b
ac = a + c
ad = a + d
bc = b + c
bd = b + d
cd = c + d

diferenca = 10**4

if ab > cd:
    if ((ab)-(cd)) < diferenca:
        diferenca = (ab)-(cd)

if ab < cd:
    if ((cd)-(ab)) < diferenca:
        diferenca = (cd)-(ab)

if ac > bd:
    if ((ac)-(bd)) < diferenca:
        diferenca = (ac)-(bd)

if ac < bd:
    if ((bd)-(ac)) < diferenca:
        diferenca = (bd)-(ac)

if ad > bc:
    if ((ad)-(bc)) < diferenca:
        diferenca = (ad)-(bc)

if ad < bc:
    if ((bc)-(ad)) < diferenca:
        diferenca = (bc)-(ad)

if ab == cd or ac == bd or ad == bc:
    print(0)
else:
    print(diferenca)