from kanren import Relation, facts, run, var

# Define a relation.
parent = Relation()

# Add facts.
facts(
    parent,
    ("john", "mary"),
    ("john", "tom"),
)

# Create a logic variable.
x = var()

# Find all values of x for which parent("john", x) is true.
print("Children of john:")
print(run(0, x, parent("john", x)))
