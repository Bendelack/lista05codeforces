consumo = int(input())

if consumo <= 10:
    print(7)
elif consumo <= 30:
    print(f'{7+((consumo-10))}')
elif consumo <= 100:
    print(f'{7+20+((consumo-30)*2)}')
else:
    print(f'{7+20+140+((consumo-100)*5)}')
# Faixa de consumo (m3) | Preço (por m3)
#   até 10	            | incluído na franquia
#   11 a 30	            | R$ 1
#   31 a 100	        | R$ 2
#   101 em diante	    | R$ 5