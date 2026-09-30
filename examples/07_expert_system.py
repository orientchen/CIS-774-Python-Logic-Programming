from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms("X, flu, fever, cough")

# Rule
flu(X) <= fever(X) & cough(X)

# Facts
+fever("john")
+cough("john")
+fever("mary")

print("People inferred to have flu:")
print(flu(X))

print("\nDoes john satisfy the flu rule?")
print(bool(flu(X) & (X == "john")))

print("\nDoes mary satisfy the flu rule?")
print(bool(flu(X) & (X == "mary")))
