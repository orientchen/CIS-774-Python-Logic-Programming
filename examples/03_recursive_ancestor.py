from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms("X, Y, Z, parent, ancestor")

+parent("John", "Mary")
+parent("Mary", "Lucy")
+parent("Lucy", "Emma")
+parent("John", "Tom")

# Base case
ancestor(X, Y) <= parent(X, Y)

# Recursive case
ancestor(X, Y) <= parent(X, Z) & ancestor(Z, Y)

print("Descendants of John:")
print(ancestor("John", Y))
