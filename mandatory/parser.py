"""
Parser utilities for polynomial expressions.

Example:
    Input:
        "5 * X^0 + 4 * X^1"
    Output:
        {0: 5, 1: 4}
"""


def normalize(expr):
    """
    Normalize a polynomial expression string.

    - Removes all spaces
    - Converts subtraction into addition of negative terms

    This transformation allows safe splitting using '+'.

    Args:
        expr (str): Polynomial expression as a string.

    Returns:
        str: Normalized expression.

    Example:
        "5 - 3*X^1"
        → "5+-3*X^1"
    """
    expr = expr.replace(" ", "")
    expr = expr.replace("-", "+-")
    if expr.startswith("+-"):
        expr = expr[1:]
    return expr

def parse_number(token):
    """
    Parse a coefficient that can be:
      - integer: "4"
      - float: "9.3"
      - fraction: "5/2", "-5/2"

    Returns:
        float
    Raises:
        ValueError if invalid
    """
    if "/" in token:
        if token.count("/") != 1:
            raise ValueError("invalid fraction")

        num_str, den_str = token.split("/")
        if num_str == "" or den_str == "":
            raise ValueError("invalid fraction")

        den = float(den_str)
        if abs(den) < 1e-12:
            raise ValueError("division by zero in fraction")

        return float(num_str) / den

    return float(token)

def parse_term(term):
    """
    Parse a single polynomial term.

    Handles:
        - Constants (e.g. "5")
        - Missing coefficients (e.g. "X", "-X")
        - Missing powers (e.g. "3*X")

    Args:
        term (str): A single polynomial term.

    Returns:
        tuple[float, int]: (coefficient, power)

    Examples:
        "4*X^2" → (4.0, 2)
        "-X"    → (-1.0, 1)
        "X"     → (1.0, 1)
        "5"     → (5.0, 0)
    """

    if "X" not in term:
        return parse_number(term), 0

    if "*" in term:
        coef = parse_number(term.split("*")[0])
    else:
        coef = -1.0 if term.startswith("-X") else 1.0

    if "^" in term:
        power = int(term.split("^")[1])
    else:
        power = 1

    return coef, power


def parse_side(expr):
    """
    Parse one side of a polynomial equation.

    Steps:
        1. Normalize expression
        2. Split into individual terms
        3. Parse each term
        4. Merge terms with the same power

    Args:
        expr (str): One side of the equation.

    Returns:
        dict[int, float]: Polynomial represented as {power: coefficient}

    Example:
        "5 + 4*X - X^2"
        → {0: 5, 1: 4, 2: -1}
    """
    terms = normalize(expr).split("+")
    poly = {}

    for term in terms:
        if term == "":
            continue
        coef, power = parse_term(term)
        poly[power] = poly.get(power, 0.0) + coef

    return poly
