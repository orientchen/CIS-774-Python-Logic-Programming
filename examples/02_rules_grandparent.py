from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms("X, Y, Z, parent, grandparent")

+parent("John", "Mary")
+parent("John", "Tom")
+parent("Mary", "Lucy")
+parent("Tom", "Sam")

# Rule: X is a grandparent of Z if X is a parent of Y
# and Y is a parent of Z.
grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)

print("Grandchildren of John:")
print(grandparent("John", Z))
