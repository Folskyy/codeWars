def alphabet_position(var):
    result = []
    for letter in var.lower():
        if 97 <= ord(letter) <= 122:
            result.append(str(ord(letter) - ord("a")))
    return f"{' '.join(result)}"

text = "You are young and life is long!"

alphabet_position(text)
