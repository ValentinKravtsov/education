import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f"Successful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error('No divide zero', exc_info=True)
        return 0

def sqrt(a):
    if a > 0:
        logging.info(f"Successful sqrt {a}")
        return a**0.5
    else:
        logging.error("number must be >= 0")
        return 0

def pow(a, b):
    return a**b


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="py.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    # print(div(3, 4))
    # print(div(3, 0))
    print(sqrt(4))
    print(sqrt(-4))