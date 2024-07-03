# Задача "Рекурсивное умножение цифр":


def get_multiplied_digits(number):
    # print(type(number), number)
    str_number = str(number)
    # print(type(str_number), len(str_number), str_number)
    first = int(str_number[0])
    # print(type(first), first)
    # print(len(str_number))

    if len(str_number) == 1:
        # print('был здесь str_number =', len(str_number))
        return number

    else:
        first = first * get_multiplied_digits(int(str_number[1:]))

    return first


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(500532)
print(result2)
