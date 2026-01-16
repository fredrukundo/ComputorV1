from math_utils import sqrt_newton, to_fraction


def solve_degree_0(c):
    if c == 0:
        return "Any real number is a solution."
    return "No solution."


def solve_degree_1(a, b):
    x = -b / a
    num, den = to_fraction(x)
    return f"The solution is:\n{num}/{den}"


def solve_degree_2(a, b, c):
    delta = b * b - 4 * a * c

    if delta > 0:
        sqrt_d = sqrt_newton(delta)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return (
            "Discriminant is strictly positive, the two solutions are:\n"
            f"{x1}\n{x2}"
        )

    if delta == 0:
        x = -b / (2 * a)
        return (
            "Discriminant is zero, the solution is:\n"
            f"{x}"
        )

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
