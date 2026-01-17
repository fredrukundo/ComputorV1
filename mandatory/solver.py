from math_utils import sqrt_newton, to_fraction


def format_float(x):
    """
    Format a floating-point number for display.

    Limits decimal precision to 6 digits if necessary,
    matching the expected output format of the subject.

    Args:
        x (float): Number to format.

    Returns:
        str: Formatted number as a string.
    """
    s = str(x)
    if "." in s and len(s.split(".")[1]) > 6:
        return f"{x:.6f}"
    return s


def solve_degree_0(c):
    """
    Solve a degree 0 equation of the form:
        c = 0

    Args:
        c (float): Constant coefficient.

    Returns:
        str: Solution message.
    """
    if c == 0:
        return "Any real number is a solution."
    return "No solution."


def solve_degree_1(a, b):
    """
    Solve a first-degree equation:
        aX + b = 0

    Args:
        a (float): Coefficient of X.
        b (float): Constant term.

    Returns:
        str: Solution message with the value of X.
    """
    x = -b / a
    return f"The solution is:\n{x}"


def solve_degree_2(a, b, c):
    """
    Solve a second-degree equation:
        aX² + bX + c = 0

    Computes the discriminant and determines the nature
    of the solutions.

    Args:
        a (float): Coefficient of X².
        b (float): Coefficient of X.
        c (float): Constant term.

    Returns:
        str: Solution message with real or complex solutions.
    """
    delta = b * b - 4 * a * c

    if delta > 0:
        sqrt_d = sqrt_newton(delta)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return (
            "Discriminant is strictly positive, the two solutions are:\n"
            f"{format_float(x1)}\n{format_float(x2)}"
        )

    if delta == 0:
        x = -b / (2 * a)
        return (
            "Discriminant is zero, the solution is:\n"
            f"{format_float(x)}"
        )

    # Complex solutions
    sqrt_d = sqrt_newton(-delta)
    real = -b / (2 * a)
    imag = sqrt_d / (2 * a)

    r_num, r_den = to_fraction(real)
    i_num, i_den = to_fraction(imag)

    return (
        "Discriminant is strictly negative, the two complex solutions are:\n"
        f"{r_num}/{r_den} + {i_num}i/{i_den}\n"
        f"{r_num}/{r_den} - {i_num}i/{i_den}"
    )
