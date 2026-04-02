"""
Lab 17: DAGs and Task Scheduling

Build a DAGNode class that represents a task with dependencies.
Nodes track their own dependencies and enforce the acyclic constraint.
"""


class CycleError(Exception):
    """Raised when adding a dependency would create a cycle."""
    pass


class DAGNode:
    class DAGNode:
    def __init__(self, name: str):
        self.name = name
        self.dependencies = set()

    def add_dependency(self, node: "DAGNode") -> None:
        if node is self:
            raise CycleError("Cannot depend on itself")

        if node.has_ancestor(self):
            raise CycleError("Would create a cycle")

        self.dependencies.add(node)

    def has_ancestor(self, target: "DAGNode") -> bool:
        visited = set()
        stack = list(self.dependencies)

        while stack:
            current = stack.pop()

            if current is target:
                return True

            if current not in visited:
                visited.add(current)
                stack.extend(current.dependencies)

        return False

    def __repr__(self):
        dep_names = sorted(d.name for d in self.dependencies)
        return f"DAGNode({self.name!r}, deps={dep_names})"
