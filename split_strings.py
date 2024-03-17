def solution(arr):
    arr2 = []
    for i in range(0, len(arr), 2): # percorre toda a palavra pulando 2 casas por vez
        arr2.append(arr[i:i+2]) # adiciona os 2 chars como um novo elemento de uma array
    if len(arr) % 2 == 1:
        arr2[-1] += '_' # adiciona um underline caso a string possua tamanho impar
    return arr2

arr = ['empty', 'corner', 'farm', 'independent']

for element in arr:
    print(solution(element))