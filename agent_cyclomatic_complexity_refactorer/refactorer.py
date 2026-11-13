"""McCabe cyclomatic complexity analyzer and refactoring advisor."""
import ast
from typing import Dict, List, Optional, Tuple, Any

class ComplexityReport:
    def __init__(self, function_name: str, complexity: int, needs_refactor: bool, suggestions: List[str]):
        self.function_name = function_name
        self.complexity = complexity
        self.needs_refactor = needs_refactor
        self.suggestions = suggestions

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1  # Base complexity

    def visit_If(self, node: ast.If):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node: ast.While):
        self.complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler):
        self.complexity += 1
        self.generic_visit(node)

class CyclomaticComplexityRefactorer:
    """Calculates McCabe cyclomatic complexity and generates decomposition plans."""

    def __init__(self, max_allowed_complexity: int = 5):
        self.max_allowed_complexity = max_allowed_complexity

    def analyze_source(self, code: str) -> List[ComplexityReport]:
        tree = ast.parse(code)
        reports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                visitor = ComplexityVisitor()
                visitor.visit(node)
                score = visitor.complexity
                needs_refactor = score > self.max_allowed_complexity
                suggestions = []

                if needs_refactor:
                    suggestions.append("Apply early return guard clauses to flatten if/else branches.")
                    suggestions.append("Extract inner loop bodies into standalone helper functions.")

                reports.append(ComplexityReport(node.name, score, needs_refactor, suggestions))

        return reports
