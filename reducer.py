# Reduce equation to = 0

def reduce_equation(left, right):
    """
        purpose:
            left  = {power: coefficient}
            right = {power: coefficient}
        then: left - right = 0
    """
    result = dict(left)

    for power, coef in right.items():
        result[power] = result.get(power, 0.0) - coef

    cleaned = {}
    for p, c in result.items():
        if abs(c) > 1e-10:
            cleaned[p] = c

    if not cleaned:
        cleaned[0] = 0.0

    return cleaned


def polynomial_degree(poly):

    """
        Return the highest power present

        ex: {0: 4, 1: 4, 2: -9.3} → 2
    """
    return max(poly.keys())


def format_number(n):
    """
        for displaying expected output format

        ex:
            4.0 = "4"
            -9.3 = "-9.3"
    """
    if abs(n - int(n)) < 1e-10:
        return str(int(n))
    return str(n)


def format_reduced(poly):
    """
        Print the reduced form exactly like the subject
    """
    parts = []
    for power in sorted(poly.keys()):
        coef = poly[power]
        coef_str = format_number(coef)
        parts.append(f"{coef_str} * X^{power}")
    return " + ".join(parts) + " = 0"

