from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms("X, parent")

# Facts
+parent("John", "Mary")
+parent("John", "Tom")
+parent("Mary", "Lucy")

# Queries
print("Children of John:")
print(parent("John", X))

print("\nParents of Lucy:")
print(parent(X, "Lucy"))
