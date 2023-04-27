n1,d1,v1 = map(int,input().split())
n2,d2,v2 = map(int,input().split())

# t1 = d1/v1
# t2 = d2/v2

if (d1/v1) < (d2/v2):
    print(n1)
elif (d2/v2) < (d1/v1):
    print(n2)

#vm = ds/t