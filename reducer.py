# Reduce equation to = 0

def reduce_equation(left, right):
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
    return max(poly.keys())


def format_number(n):
    if abs(n - int(n)) < 1e-10:
        return str(int(n))
    return str(n)


def format_reduced(poly):
    parts = []
    for power in sorted(poly.keys()):
        coef = poly[power]
        coef_str = format_number(coef)
        parts.append(f"{coef_str} * X^{power}")
    return " + ".join(parts) + " = 0"

