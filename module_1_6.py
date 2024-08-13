# словарь
my_dict = {'Roman': 1989, 'Alex': 1983, 'Daniil': 2012}
print('Dict:', my_dict)
print('Existing value:',my_dict['Daniil'])
print('Not existing value:', my_dict.get('Barbara'))
my_dict.update({'Anton': 1995,
                'Kirill': 2001})
print('Updated dictionary:', my_dict)
name_year = my_dict.pop('Alex')
print('Deleted value:', name_year)
print('Modified dictionary:', my_dict)

# множество
my_set = {'education', 'work', 2024, False, False, 888, True, 'work'}
print('Set: ', my_set)
my_set.add('SHIP')
print('Modified set: ', my_set)