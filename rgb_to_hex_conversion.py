def solution(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
        
    return ('' + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]).upper()

# 255, 255, 255
# 255, 255, 300
# 0, 0, 0
# 148, 0, 211

r = 255
g = 255
b = 300

solution(r, g, b)