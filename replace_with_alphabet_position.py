def alphabet_position(var):
    result = []
    for letter in var.lower():
        if 97 <= ord(letter) <= 122:
            result.append(str(ord(letter) - ord("a")))
    return f"{' '.join(result)}"

with open('input/alphabet_position_input.txt', 'r') as f:
    entrada = f.read()

with open('output/alphabet_position_output.txt', 'w') as f:
    f.write(f"{alphabet_position(entrada)}\n")