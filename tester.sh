############################################################
# ComputorV1 — Evaluation Script
# Run this from your project root.
# Assumes you have:
#   mandatory/main.py
#   bonus/main.py
############################################################

echo "=============================="
echo "MANDATORY TESTS"
echo "=============================="
cd mandatory || exit 1

echo ""
echo "[M0] CLI / basic input checks"
python3 main.py
python3 main.py "X^2 + 1"

echo ""
echo "[M1] Subject main example (degree 2, Δ > 0)"
python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

echo ""
echo "[M2] Reduced form sign formatting (+ - should not appear)"
python3 main.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

echo ""
echo "[M3] Degree 0 — infinite solutions"
python3 main.py "42 * X^0 = 42 * X^0"

echo ""
echo "[M4] Degree 0 — no solution"
python3 main.py "4 * X^0 = 8 * X^0"

echo ""
echo "[M5] Degree 1 — simple linear"
python3 main.py "0 * X^0 + 2 * X^1 = 4 * X^0"

echo ""
echo "[M6] Degree 1 — negative slope"
python3 main.py "1 * X^0 = 3 * X^0 - 2 * X^1"

echo ""
echo "[M7] Degree 2 — easy real roots (Δ > 0, roots 2 and 3)"
python3 main.py "1 * X^2 - 5 * X^1 + 6 * X^0 = 0 * X^0"

echo ""
echo "[M8] Degree 2 — double root (Δ = 0, root 1)"
python3 main.py "1 * X^2 - 2 * X^1 + 1 * X^0 = 0 * X^0"

echo ""
echo "[M9] Degree 2 — complex roots (Δ < 0)"
python3 main.py "1 * X^2 + 0 * X^1 + 1 * X^0 = 0 * X^0"

echo ""
echo "[M10] Degree > 2 — must refuse"
python3 main.py "1 * X^3 + 1 * X^0 = 0 * X^0"

echo ""
echo "[M11] Zero coefficients stress (no crash)"
python3 main.py "0 * X^0 + 0 * X^1 + 0 * X^2 = 0 * X^0"

echo ""
echo "[M12] Decimals stress"
python3 main.py "5.5 * X^0 = 4 * X^0 + 7.2 * X^1"

echo ""
echo "[M13] Fractions in input (only if you chose to support them in mandatory)"
python3 main.py "5/2 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
python3 main.py "5/0 * X^0 = 0 * X^0"   # should NOT traceback (clean error)

cd .. || exit 1


echo ""
echo "=============================="
echo "BONUS TESTS"
echo "=============================="
cd bonus || exit 1

echo ""
echo "[B0] Natural input: constants / X without coef / missing exponent"
python3 main.py "4 = 0"
python3 main.py "X = 0"
python3 main.py "4 * X = 8"

echo ""
echo "[B1] Natural input: missing coefficient (X^n means 1*X^n)"
python3 main.py "X^2 = X^2"

echo ""
echo "[B2] Free-form: spaces + mixed forms"
python3 main.py "5 + 4 * X + X^2 = X^2"

echo ""
echo "[B3] Free-form: missing middle degree (must not KeyError)"
python3 main.py "X^2 + 1 = 0"

echo ""
echo "[B4] Duplicate powers + merge terms"
python3 main.py "X^2 + 2 + 3*X + X^2 - X = 0"

echo ""
echo "[B5] Implicit multiplication (only if you implemented 2X support)"
python3 main.py "2X + 1 = 0"

echo ""
echo "[B6] Error handling: invalid variables / garbage tokens (no traceback)"
python3 main.py "5 + Y = 0"
python3 main.py "5 + x = 0"
python3 main.py "5 + Xxx^2 = 0"

echo ""
echo "[B7] Error handling: syntax mistakes (no traceback)"
python3 main.py "5 + + X = 0"
python3 main.py "X^^2 = 0"
python3 main.py "X^ = 0"
python3 main.py "= X + 1"
python3 main.py "X + 1"

echo ""
echo "[B8] Fractions output (when applicable)"
python3 main.py "2X = 1"

echo ""
echo "[B9] Complex + fraction-friendly case (often yields rational parts)"
python3 main.py "4X^2 + 4X + 5 = 0"

echo ""
echo "[B10] Intermediate steps check (should show parse/reduce/discriminant steps)"
python3 main.py "1 * X^2 - 5 * X + 6 = 0"

cd .. || exit 1

echo ""
echo "DONE."
