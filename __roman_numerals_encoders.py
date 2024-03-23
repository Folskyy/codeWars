def solucao(num):
    solv = ''
    char = ['M', 'CM', 'D ','CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    alg = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    for i in range(0, len(alg)):
        x = num // alg[i]
        solv += char[i] * x
        num %= alg[i]

    return ''.join(solv)

teste = 1990

print(solucao(teste))
    








# def solution(num):
#     solv = ''
#     x = num // 1000
#     num %= 1000
#     solv += x * 'M'

#     x = num // 500
#     if x == 4:
#         solv += 'CD'
#     num %= 500
#     solv += x * 'D'
    
#     x = num // 100
#     num %= 100
#     solv += x * 'C'
    
#     x = num // 50
#     num %= 50
#     solv += x * 'L'
    
#     x = num // 10
#     num %= 10
#     solv += x * 'X'
    
#     x = num // 5
#     num %= 5
#     solv += x * 'V'
    
#     solv += num * 'I'