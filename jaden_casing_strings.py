def to_jaden_case(string):
    words = string.lower().split()
    title_case = [word.capitalize() for word in words]

    return ' '.join(title_case)
frase = "How can mirrors be real if our eyes aren't real"

print(to_jaden_case(frase))
