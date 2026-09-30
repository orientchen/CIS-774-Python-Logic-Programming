# CIS 774 — Python Logic Programming

This repository contains Python examples for the **Logic Programming** module in CIS 774 Programming Paradigms.

## Main Idea

Python is a general-purpose programming language and does not natively provide the facts, rules, logic variables, and queries associated with logic programming.

For this module:

- **pyDatalog** is the main library used to demonstrate facts, rules, queries, inference, and recursion.
- **kanren** is included only as a brief example of another relational / miniKanren-style approach.

The goal is to study the **logic programming paradigm**, not to learn many Python libraries.

## Examples

| File | Topic |
|---|---|
| `01_facts_queries.py` | Facts and queries with pyDatalog |
| `02_rules_grandparent.py` | Rules and inference |
| `03_recursive_ancestor.py` | Recursive rules |
| `04_sibling_rules.py` | Rule-based relationships |
| `05_kanren_relations.py` | Brief relational-programming comparison with kanren |
| `06_expert_system.py` | Simple rule-based expert system |
| `07_recursive_path.py` | Recursive path reasoning |

## Run in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Wait for the Codespace to finish setting up. The required packages are installed automatically.
4. Open a terminal.

Run the examples in order:

```bash
python examples/01_facts_queries.py
python examples/02_rules_grandparent.py
python examples/03_recursive_ancestor.py
python examples/04_sibling_rules.py
python examples/05_kanren_relations.py
python examples/06_expert_system.py
python examples/07_recursive_path.py
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

## Transition to Prolog

Python requires libraries such as pyDatalog or kanren to support logic-programming ideas. Prolog is designed specifically for logic programming, so facts, rules, queries, unification, and inference are central features of the language.
