def square_or_square_root (list):
    from math import sqrt 
    from math import pow
    
    for i in range(len(list)):
        if (sqrt(list[i]) % 1 == 0.000):
            list[i] = int(sqrt(list[i]))
        else:
            list[i] = int(pow(list[i], 2))

    for i in range(len(list)):
        list[i] = int(list[i])

    return list