def is_prime_number(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        print(is_prime_number(1))
        print(is_prime_number(2))
        print(is_prime_number(20))
    except e:
        print(e)
