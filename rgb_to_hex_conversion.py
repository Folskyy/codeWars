def rgb(r, g, b):
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
        
    return ('' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)).upper()

# def rgb(r, g, b):
#     clamp = lambda x: max(0, min(x, 255))
#     return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))

r = 148
g = 0
b = 211

rgb(r, g, b)