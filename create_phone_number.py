def create_phone_number(n):
    res = '('
    for i in range(0, 10):
        if i == 3:
            res += ') '
        if i == 6:
            res += '-'
        res += str(n[i])
    return res

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(create_phone_number(num))