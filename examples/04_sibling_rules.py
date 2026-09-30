from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms("X, Y, P, parent, sibling")

+parent("John", "Mary")
+parent("John", "Tom")
+parent("Alice", "Mary")
+parent("Alice", "Tom")
+parent("Mary", "Lucy")

# In this example, siblings are different people who share
# at least one parent. This definition therefore includes half-siblings.
sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)

print("Sibling relationships:")
print(sibling(X, Y))
