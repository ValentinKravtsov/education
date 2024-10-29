def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        i = 2
        while i < result:
            if result % i == 0:
                print('Число составное')
                return result
            i += 1
        print('Число простое')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
