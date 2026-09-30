from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms("X, Y, Z, connected, path")

+connected("a", "b")
+connected("b", "c")
+connected("c", "d")
+connected("b", "d")

# Base case: a direct connection is a path.
path(X, Y) <= connected(X, Y)

# Recursive case: X reaches Z if X connects to Y
# and Y has a path to Z.
path(X, Z) <= connected(X, Y) & path(Y, Z)

print("Is there a path from a to d?")
print(bool(path("a", "d")))

print("\nIs there a path from c to a?")
print(bool(path("c", "a")))

print("\nNodes reachable from a:")
print(path("a", Y))
