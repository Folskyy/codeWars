def make_readable(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"


# print(make_readable(0)) # , "00:00:00")
# print(make_readable(59)) # , "00:00:59")
# print(make_readable(60)) # , "00:01:00")
# print(make_readable(3599)) # , "00:59:59")
# print(make_readable(3600)) # , "01:00:00")
# print(make_readable(86399)) # , "23:59:59")
# print(make_readable(86400)) # , "24:00:00")
# print(make_readable(359999)) # , "99:59:59")
    