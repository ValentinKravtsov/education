def count_calls():
    global calls
    calls += 1


def string_info(word):
    count_calls()
    return len(word), word.upper(), word.lower()


def is_contains(word_2, list_to_search):
    count_calls()
    for i in list_to_search:
        if word_2.lower() == i.lower():
            return True
        else:
            return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
