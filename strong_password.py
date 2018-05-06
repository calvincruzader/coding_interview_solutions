data_file = open('./data/strong_password_data.txt', 'r')


def minimum_number(n, password):
    n = int(n)
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # add each specification
    result = 4
    for c in password:
        if c in numbers:
            result -= 1
            break

    for c in password:
        if c in lower_case:
            result -= 1
            break

    for c in password:
        if c in upper_case:
            result -= 1
            break

    for c in password:
        if c in special_characters:
            result -= 1
            break

    # is it 6?
    if n < 6:
        num_remaining = 6 - (n + result)
        if num_remaining > 0: result += num_remaining
    return result


with data_file:
    n = data_file.readline()
    password = data_file.readline()

    answer = minimum_number(n, password)
    print(answer)
