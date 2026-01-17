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
    Convert a polynomial dict to a nicely formatted string.

    - Omits * X^0 for constants
    - Shows X instead of X^1
    - Omits 1* in front of X
    """
    parts = []

    for power in sorted(poly.keys()):
        coef = poly[power]

        # Skip zero coefficients (shouldn't happen after reduction, but safe)
        if abs(coef) < 1e-10:
            continue

        # Format coefficient
        coef_str = format_number(abs(coef))
        if coef_str == "1" and power != 0:
            coef_str = ""  # omit 1 in front of X

        # Format term
        if power == 0:
            term = f"{coef_str}"
        elif power == 1:
            term = f"{coef_str}X"
        else:
            term = f"{coef_str}X^{power}"

        # Add sign
        if coef < 0:
            parts.append(f"- {term}")
        else:
            parts.append(f"+ {term}")

    # Remove leading "+"
        if parts[0].startswith("+ "):
            parts[0] = parts[0][2:]

    return " ".join(parts) + " = 0"