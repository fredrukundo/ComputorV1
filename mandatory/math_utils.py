def abs_val(x):
    return x if x >= 0 else -x


def sqrt_newton(n, precision=1e-10):
    """
    This function is used to compute the square root of the
    discriminant when solving second-degree equations.
    """
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


def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two integers
    using the Euclidean algorithm.
    - gcd(a,b)= gcd(b,a mod b)

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.

    This function is used to simplify fractions when displaying
    exact results.
    """
    a = abs_val(a)
    b = abs_val(b)
    while b != 0:
        a, b = b, a % b
    return a


def to_fraction(x):
    """
    Convert a floating-point number into fraction.

    This function is mainly intended for the -delta (complex numbers),
    allowing exact display of solutions such as:
        -1/5 + 2i/5
    """
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
