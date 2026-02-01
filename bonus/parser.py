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
    if not isinstance(eq, str) or not eq.strip():
        raise ValueError("empty equation")

    eq = eq.replace(" ", "")

    # exactly one '='
    if eq.count("=") != 1:
        raise ValueError("equation must contain exactly one '='")

    left, right = eq.split("=")
    if left == "" or right == "":
        raise ValueError("missing left or right side")

    # reject alternative power syntaxes
    if "**" in eq or "^^" in eq:
        raise ValueError("invalid power syntax (use '^')")

    # allow only digits, X, operators, dot, caret
    allowed = set("0123456789X+-*/.^")
    bad = {ch for ch in eq if ch not in allowed}
    if bad:
        raise ValueError(f"invalid character(s): {''.join(sorted(bad))}")

    if "Y" in eq or "Z" in eq:
        raise ValueError("invalid variable (only X is allowed)")

    if "XX" in eq:
        raise ValueError("invalid variable usage")

    forbidden_pairs = ["++", "+*", "+/", "+^",
                       "-*", "-/", "-^",
                       "*+", "**", "*/", "*^",
                       "/+", "/*", "//", "/^",
                       "^+", "^*", "^/", "^^"]
    for p in forbidden_pairs:
        if p in eq:
            raise ValueError(f"invalid operator sequence: '{p}'")

    i = 0
    while i < len(eq):
        if eq[i] == "^":
            if i == len(eq) - 1:
                raise ValueError("missing exponent after '^'")
            j = i + 1
            if eq[j] == "-":
                j += 1
            if j == len(eq) or not eq[j].isdigit():
                raise ValueError("exponent after '^' must be an integer")
            while j < len(eq) and eq[j].isdigit():
                j += 1
            i = j
        else:
            i += 1

