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
    precision = 1000000
    num = int(x * precision)
    den = precision

    g = gcd(abs_val(num), den)
    return num // g, den // g