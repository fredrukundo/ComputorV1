# Math tools we are allowed to use

def abs_val(x):
    return x if x >= 0 else -x


def sqrt_newton(n, precision=1e-10):
    if n < 0:
        return None
    if n == 0:
        return 0
    x = n
    while True:
        root = 0.5 * (x + n / x)
        if abs_val(root - x) < precision:
            return root
        x = root

# to reduce fractions (boonus part)
def gcd(a, b):
    a = abs_val(a)
    b = abs_val(b)
    while b != 0:
        a, b = b, a % b
    return a

# float to irreducible fraction (bonus) => 0.4 = 2/5
def to_fraction(x):
    precision = 1e-6
    sign = -1 if x < 0 else 1
    x = abs_val(x)

    numerator = x
    denominator = 1

    while abs_val(numerator - round(numerator)) > precision:
        numerator *= 10
        denominator *= 10

    numerator = int(round(numerator))
    g = gcd(numerator, denominator)
    return sign * (numerator // g), denominator // g
