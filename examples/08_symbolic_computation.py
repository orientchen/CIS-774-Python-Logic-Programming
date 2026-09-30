# Symbolic computation with SymPy

from sympy import symbols, diff, simplify, expand

# Create a symbolic variable
x = symbols("x")

# Define a symbolic expression
f = x**3 + 2*x**2 - 5*x + 1

print("Expression:")
print(f)

# Symbolic differentiation
print("\nDerivative:")
print(diff(f, x))

# Symbolic substitution
print("\nValue when x = 2:")
print(f.subs(x, 2))

# Symbolic expansion
expression = (x + 1) ** 3
print("\nBefore expansion:")
print(expression)

print("\nAfter expansion:")
print(expand(expression))

# Symbolic simplification
expression2 = (x**2 - 1) / (x - 1)
print("\nSimplified expression:")
print(simplify(expression2))
