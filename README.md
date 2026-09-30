# CIS 774 — Python Logic Programming

This repository contains Python examples for the **Logic Programming** module in CIS 774 Programming Paradigms.

## Topics

The examples progress from basic facts and queries to rules, recursion, relational programming, symbolic logic, and small applications.

| File | Topic |
|---|---|
| `01_facts_queries.py` | Facts and queries with pyDatalog |
| `02_rules_grandparent.py` | Rules and inference |
| `03_recursive_ancestor.py` | Recursive rules |
| `04_sibling_rules.py` | Rule-based relationships |
| `05_kanren_relations.py` | Relational programming with kanren |
| `06_sympy_logic.py` | Symbolic/propositional logic with SymPy |
| `07_expert_system.py` | Simple rule-based expert system |
| `08_recursive_path.py` | Recursive path reasoning |

## Run in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Wait for the Codespace to finish setting up. The required Python packages are installed automatically.
4. Open a terminal.

Run an example with:

```bash
python examples/01_facts_queries.py
```

Then continue with:

```bash
python examples/02_rules_grandparent.py
python examples/03_recursive_ancestor.py
python examples/04_sibling_rules.py
python examples/05_kanren_relations.py
python examples/06_sympy_logic.py
python examples/07_expert_system.py
python examples/08_recursive_path.py
```

## Logic Programming Idea

In imperative programming, we usually describe **how** to perform a computation.

In logic programming, we describe **facts and rules**, then ask the system to find values that satisfy those relationships.

For example:

```python
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= parent(X, Z) & ancestor(Z, Y)
```

The first rule is the base case. The second rule recursively defines a more distant ancestor.

## Libraries

- **pyDatalog** — Datalog-style facts, rules, queries, and recursion
- **kanren** — relational/miniKanren-style programming
- **SymPy** — symbolic and propositional logic

SymPy is included to demonstrate formal symbolic logic; it is not the same relational logic-programming model used by pyDatalog and kanren.
