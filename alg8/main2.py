import random


def generate_key_pair():
    # Генерация случайных простых чисел p и q
    p = generate_prime_number()
    q = generate_prime_number()

    # Вычисление n
    n = p * q

    # Вычисление значения функции Эйлера от n
    phi = (p - 1) * (q - 1)

    # Генерация открытой экспоненты e
    e = generate_public_exponent(phi)

    # Вычисление секретной экспоненты d
    d = modular_inverse(e, phi)

    # Возвращение открытого и секретного ключей
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


def generate_prime_number():
    # Генерация случайного числа
    prime_candidate = random.randint(2 ** 16, 2 ** 17)

    # Проверка числа на простоту
    while not is_prime(prime_candidate):
        prime_candidate += 1

    return prime_candidate


def is_prime(n):
    # Проверка числа на простоту
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def generate_public_exponent(phi):
    # Генерация открытой экспоненты e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e


def gcd(a, b):
    # Нахождение наибольшего общего делителя двух чисел
    while b != 0:
        a, b = b, a % b
    return a


def modular_inverse(a, m):
    # Нахождение модулярного обратного элемента
    _, x, _ = extended_gcd(a, m)
    return x % m


def extended_gcd(a, b):
    # Расширенный алгоритм Евклида
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y


def encrypt(message, public_key):
    # Шифрование сообщения
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key):
    # Расшифровка сообщения
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message


message = input("Введите сообщение: ")

public_key, private_key = generate_key_pair()
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Открытый ключ:", public_key)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
