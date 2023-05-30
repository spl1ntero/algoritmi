def extended_euclidean_algorithm(a, b):
    x, y = 0, 1
    last_x, last_y = 1, 0
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x, last_x = last_x - quotient * x, x
        y, last_y = last_y - quotient * y, y
    return a, last_x, last_y


a = int(input())
b = int(input())
gcd, x, y = extended_euclidean_algorithm(a, b)
print("НОД чисел", a, "и", b, "равен", gcd)
print("Коэффициенты х и у, такие что a*x + b*y = gcd(", a, ",", b, "):", x, y)
