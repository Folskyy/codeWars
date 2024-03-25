def solution(num):
    solv = ''
    char = ['M', 'CM', 'D ','CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    alg = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    for i in range(0, len(alg)):
        x = num // alg[i]
        solv += char[i] * x
        num %= alg[i]

    return ''.join(solv)

teste = 1990

print(solution(teste))