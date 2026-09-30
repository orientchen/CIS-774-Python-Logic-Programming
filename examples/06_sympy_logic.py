from sympy import symbols
from sympy.logic.boolalg import And, Not, Implies
from sympy.logic.inference import satisfiable

A, B = symbols("A B")

# (A -> B) AND A
expr = And(Implies(A, B), A)

print("Expression:")
print(expr)

print("\nA satisfying assignment:")
print(satisfiable(expr))

print("\nContradiction A AND NOT A:")
print(satisfiable(And(A, Not(A))))
