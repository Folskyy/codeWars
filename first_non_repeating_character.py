def first_non_repeating_letter(s):
    for i in range(0, len(s)):
        if s[i].lower() not in s[i+1:].lower() and s[i].lower() not in s[:i].lower():
            return s[i]
    return ''

arr = ['stress', 'sTreSS']
for element in arr:
    print(first_non_repeating_letter(element))
