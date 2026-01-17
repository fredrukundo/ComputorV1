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


def sqrt_newton(n, precision=1e-10):
    """
    Compute the square root of a non-negative number using
    Newton's (Babylonian) method.

    Args:
        n (float): The number whose square root is computed.
        precision (float): The stopping threshold for convergence.

    Returns:
        float | None:
            - The square root of n if n >= 0
            - None if n is negative

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

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of a and b.

    This function is used to simplify fractions when displaying
    exact or irreducible results.
    """
    a = abs_val(a)
    b = abs_val(b)
    while b != 0:
        a, b = b, a % b
    return a


def to_fraction(x):
    """
    Convert a floating-point number into an irreducible fraction.

    Args:
        x (float): The floating-point number to convert.

    Returns:
        tuple[int, int]: A tuple (numerator, denominator) representing
        the irreducible fraction.

    This function is mainly intended for the bonus part of the project,
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
