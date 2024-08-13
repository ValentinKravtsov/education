immutable_var = ('education', 2024, False, [15, 'Rocket'])
print(immutable_var)
# элементы кортежа изменять нельзя
# immutable_var[3] = 15
mutable_list = ['education', 2024, False]
print(mutable_list)
mutable_list[0] = 39
mutable_list[1] = True
mutable_list[2] = 'work'
print(mutable_list)