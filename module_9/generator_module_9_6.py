def all_variants(text):
    i = 0
    while i <= len(text):
        y = 1
        while i+y <= len(text):
            yield text[i:i+y]
            y += 1
        i += 1


a = all_variants("geeks")
for i in a:
    print(i)
