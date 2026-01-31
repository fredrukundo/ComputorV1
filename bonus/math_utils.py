def abs_val(x):
    """
    Compute the absolute value of a number.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: x if x is positive or zero, otherwise -x.

    This function replaces the built-in abs() to comply
    with the project restriction of not using math libraries.
    """
    return x if x >= 0 else -x

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def to_fraction(x):
    precision = 1000000
    num = int(x * precision)
    den = precision

    g = gcd(abs_val(num), den)
    return num // g, den // g


def sqrt_newton(x):
    if x == 0:
        return 0
    guess = x
    for _ in range(50):
        guess = (guess + x / guess) / 2
    return guess
