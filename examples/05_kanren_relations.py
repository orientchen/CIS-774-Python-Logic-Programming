from kanren import Relation, facts, run, var, lall

parent = Relation()
facts(
    parent,
    ("john", "mary"),
    ("mary", "susan"),
    ("john", "tom"),
)

x, y, z = var(), var(), var()

def grandparent(person, grandchild):
    return lall(parent(person, y), parent(y, grandchild))

print("Children of john:")
print(run(0, x, parent("john", x)))

print("\nGrandparents of susan:")
print(run(0, x, grandparent(x, "susan")))
