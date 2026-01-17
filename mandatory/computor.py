import sys
from parser import parse_side
from reducer import reduce_equation, polynomial_degree, format_reduced
from solver import solve_degree_0, solve_degree_1, solve_degree_2


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 computor.py \"equation\"")
        return

    equation = sys.argv[1]

    if "=" not in equation:
        print("Invalid equation")
        return

    left_str, right_str = equation.split("=")

    left = parse_side(left_str)
    right = parse_side(right_str)

    reduced = reduce_equation(left, right)

    print("Reduced form:", format_reduced(reduced))

    degree = polynomial_degree(reduced)
    
    if degree != 0:
        print("Polynomial degree:", degree)

    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        return

    if degree == 0:
        print(solve_degree_0(reduced.get(0, 0)))
        return

    if degree == 1:
        a = reduced.get(1, 0)
        b = reduced.get(0, 0)
        print(solve_degree_1(a, b))
        return

    if degree == 2:
        a = reduced.get(2, 0)
        b = reduced.get(1, 0)
        c = reduced.get(0, 0)
        print(solve_degree_2(a, b, c))


if __name__ == "__main__":
    main()
