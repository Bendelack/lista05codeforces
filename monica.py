monica = int(input())
filho1 = int(input())
filho2 = int(input())
filho3 = monica - (filho1 + filho2)

if filho1 > filho2 and filho1 > filho3:
    print(filho1)
elif filho2 > filho1 and filho2 > filho3:
    print(filho2)
elif filho3 > filho2 and filho3 > filho1:
    print(filho3)