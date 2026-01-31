# Reduce equation to = 0
from math_utils import abs_val

def reduce_equation(left, right):
    """
    Reduce a polynomial equation to a single polynomial equal to zero.

    Computes:
        left - right = 0

    Args:
        left (dict[int, float]): Left side polynomial {power: coefficient}
        right (dict[int, float]): Right side polynomial {power: coefficient}

    Returns:
        dict[int, float]: Reduced polynomial with all powers filled,
                          including zero coefficients if necessary.

    Notes:
        - Coefficients close to zero are removed (floating-point safety)
        - If all terms cancel, returns {0: 0.0}
    """
    result = dict(left)

    for power, coef in right.items():
        result[power] = result.get(power, 0.0) - coef

    cleaned = {}
    for p, c in result.items():
        if abs_val(c) > 1e-10:
            cleaned[p] = c

    if not cleaned:
        cleaned[0] = 0.0
    else:
        max_degree = max(result.keys())
        for p in range(0, max_degree + 1):
            if p not in cleaned:
                cleaned[p] = 0.0

    return cleaned


def polynomial_degree(poly):
    """
    Compute the degree of a polynomial.

    Args:
        poly (dict[int, float]): Polynomial {power: coefficient}

    Returns:
        int: Highest power present in the polynomial.

    Example:
        {0: 4, 1: 4, 2: -9.3} → 2
    """
    return max(poly.keys())


def format_number(n):
    """
    Format a number for display.

    Converts floats that represent integers into integer strings.

    Args:
        n (float): Number to format.

    Returns:
        str: Formatted number as a string.

    Examples:
        4.0   → "4"
        -9.3  → "-9.3"
    """
    if abs(n - int(n)) < 1e-10:
        return str(int(n))
    return str(n)


def format_reduced(poly):
    """
    Format a reduced polynomial for display.

    Args:
        poly (dict[int, float]): Reduced polynomial {power: coefficient}

    Returns:
        str: Human-readable reduced form ending with '= 0'.

    Example:
        {0: 4, 1: 4, 2: -9.3}
        → "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
    """
    parts = []

    for power in sorted(poly.keys()):
        coef = poly[power]
        coef_str = format_number(abs_val(coef))

        if coef < 0:
            parts.append(f"- {coef_str} * X^{power}")
        else:
            parts.append(f"+ {coef_str} * X^{power}")

    # remove leading "+"
    if parts[0].startswith("+ "):
        parts[0] = parts[0][2:]

    return " ".join(parts) + " = 0"
