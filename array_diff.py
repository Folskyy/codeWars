def array_diff(a, b):
    res = []
    
    for elemento in a:
        if elemento not in b:
            res.append(elemento)

    return res

list1 = [0, 2, 3, 4, 2, 2, 2, 3, 6, 7, 8, 9, 0]
list2 = [0, 2, 3]

print(array_diff(list1, list2))
