def is_valid_part(part):
    try:
        number = int(part)
    except ValueError:
        return False

    if number < 0 or number > 255:
        return False

    if len(part) > 1 and part[0] == "0":
        return False

    return True


print(is_valid_part("255"))
print(is_valid_part("256"))
print(is_valid_part("01"))
print(is_valid_part("0"))


def is_valid_ip(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for p in parts:
        if not is_valid_part(p):
            return False

    return True


print(is_valid_ip("192.168.1.1"))
print(is_valid_ip("192.168.256.1"))
print(is_valid_ip("192.168.1"))
print(is_valid_ip("192.168.01.1"))


def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    remainder = n % 2
    quotient = n // 2

    return decimal_to_binary(quotient) + str(remainder)


print(decimal_to_binary(10))
print(decimal_to_binary(255))
print(decimal_to_binary(1))


def binary_to_decimal(b):
    if b == "":
        return 0

    bit = int(b[0])
    place_value = 2 ** (len(b) - 1)
    value = bit * place_value

    return value + binary_to_decimal(b[1:])


print(binary_to_decimal("1010"))
print(binary_to_decimal("11111111"))
print(binary_to_decimal("1"))