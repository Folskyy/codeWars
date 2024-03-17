def alphabet_position(var):
    result = []
    for letter in var.lower():
        if 97 <= ord(letter) <= 122:
            result.append(str(ord(letter) - ord()))
    return f"{' '.join(result)}"