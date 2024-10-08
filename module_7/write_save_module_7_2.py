def custom_write(file_name: str, strings: list):
    dict_pos = {}
    str_ = 1
    file = open(file_name, 'a', encoding="utf-8")
    for i in strings:
        dict_pos[(str_, file.tell())] = i
        file.write(f"{i}\n")
        str_ += 1
    return dict_pos


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

