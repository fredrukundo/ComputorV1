# # this file is for parsing the string.
# """
#     "5 * X^0 + 4 * X^1"
#         ↓
#     {0: 5, 1: 4}
# """

def insert_implicit_mul(expr: str) -> str:
    """
    Turn implicit number-variable multiplication into explicit '*':
      "2X" -> "2*X"
      "-3.5X" -> "-3.5*X"
    Minimal: only handles number immediately followed by X.
    """
    s = expr.replace(" ", "")
    out = []
    n = len(s)

    for i, ch in enumerate(s):
        out.append(ch)
        if i + 1 < n and s[i + 1] == "X" and (ch.isdigit() or ch == "."):
            out.append("*")

    return "".join(out)

def normalize(expr):
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
    # constant term
    if "X" not in term:
        return parse_number(term), 0

    # coefficient
    if "*" in term:
        coef_part, x_part = term.split("*")
        coef = parse_number(coef_part)
    else:
        if term.startswith("-X"):
            coef = -1.0
        else:
            coef = 1.0
        x_part = term[1:] if term.startswith("-") else term[1:]

    # power
    if "^" in term:
        power = int(term.split("^")[1])
    else:
        power = 1

    return coef, power


def parse_side(expr):
    terms = normalize(expr).split("+")
    poly = {}

    for term in terms:
        if term == "":
            continue
        coef, power = parse_term(term)
        poly[power] = poly.get(power, 0.0) + coef

    return poly

def validate_equation(eq: str) -> None:
    """
    validation for polynomial equation.

    Raises ValueError if invalid.
    """

    if not isinstance(eq, str) or not eq.strip():
        raise ValueError("empty equation")

    # Must contain exactly one '='
    if eq.count("=") != 1:
        raise ValueError("equation must contain exactly one '='")

    # Allowed characters
    allowed = set("0123456789X+-*/.^= ")

    for ch in eq:
        if ch not in allowed:
            raise ValueError(f"invalid character: '{ch}'")

    # Invalid variable (only uppercase X allowed)
    if "x" in eq:
        raise ValueError("invalid variable (use uppercase X only)")

    # Invalid operator sequences
    compact = eq.replace(" ", "")
    if "++" in compact or "--" in compact:
        raise ValueError("invalid operator sequence")

    if "**" in compact or "^^" in compact:
        raise ValueError("invalid power syntax")

    # Cannot start or end with '='
    left, right = eq.split("=")
    if not left.strip() or not right.strip():
        raise ValueError("missing expression on one side")
