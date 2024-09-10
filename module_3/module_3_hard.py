def calculate_structure_sum(data, count=0):
    if isinstance(data, int):
        return data
    if isinstance(data, str):
        return len(data)
    for i in data:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            if len(i) == 0:
                continue
            count += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                count += calculate_structure_sum(key)
                count += calculate_structure_sum(value)
        elif isinstance(i, str):
            count += len(i)
        else:
            count += i
    return count


data_structure = [
          [1, 2, 3],
          {'a': 4, 'b': 5},
          (6, {'cube': 7, 'drum': 8}),
          "Hello",
          ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
print('Сумма всех чисел и строк: ', calculate_structure_sum(data_structure))
