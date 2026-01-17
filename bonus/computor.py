import sys
from parser import parse_side, validate_equation
from reducer import reduce_equation, format_reduced, polynomial_degree
from solver import solve_degree_0, solve_degree_1, solve_degree_2

def main():

    try:
        if len(sys.argv) != 2:
            print("Usage: python3 computor.py \"equation\"")
            return
        equation = sys.argv[1]
        
        validate_equation(equation)
        print("Parsing equation...")
        left_expr, right_expr = equation.split("=")

        left = parse_side(left_expr)
        right = parse_side(right_expr)

        print("Reducing equation...")
        reduced = reduce_equation(left, right)

        print("Reduced form:", format_reduced(reduced))

        degree = polynomial_degree(reduced)

        if degree > 2:
            print("Polynomial degree:", degree)
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            return

        if degree == 0:
            print(solve_degree_0(reduced.get(0, 0)))
            return

        if degree == 1:
            print("Polynomial degree: 1")
            a = reduced[1]
            b = reduced[0]
            print(solve_degree_1(a, b))
            return

        if degree == 2:
            print("Polynomial degree: 2")
            a = reduced.get(2, 0.0)
            b = reduced.get(1, 0.0)
            c = reduced.get(0, 0.0)
            print(solve_degree_2(a, b, c))

    except ValueError as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
