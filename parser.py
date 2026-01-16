# this file is for parsing the string.
"""
    "5 * X^0 + 4 * X^1"
        ↓
    {0: 5, 1: 4}
"""

def normalize(expr):
    """
        Removes spaces
        Converts - into +- to simplify splitting

        Example:
            "5 - 3*X^1"
            → "5+-3*X^1"
        This allows safe splitting by "+"
    """
    expr = expr.replace(" ", "")
    expr = expr.replace("-", "+-")
    if expr.startswith("+-"):
        expr = expr[1:]
    return expr


def parse_term(term):
    """
        Handles missing coefficients
        Handles missing powers
        Handles constants

        Example:
            "4*X^2" → (4.0, 2)
            "-X"    → (-1.0, 1)
            "5"     → (5.0, 0)

        Return:
            (coefficient, power)
    """

    if "X" not in term:
        return float(term), 0

    if "*" in term:
        coef = float(term.split("*")[0])
    else:
        coef = -1.0 if term.startswith("-X") else 1.0

    if "^" in term:
        power = int(term.split("^")[1])
    else:
        power = 1

    return coef, power


def parse_side(expr):
    """
        - Parse one side of the equation
        - Return polynomial dictionary

        example:
            "5 + 4*X - X^2"
            → {0: 5, 1: 4, 2: -1}

        Normalize, Split into terms, Parse each term and Merge same powers
    """

    terms = normalize(expr).split("+")
    poly = {}

    for term in terms:
        if term == "":
            continue
        coef, power = parse_term(term)
        poly[power] = poly.get(power, 0.0) + coef

    return poly
