"""Unit tests for agent-cyclomatic-complexity-refactorer."""
import unittest
from agent_cyclomatic_complexity_refactorer.refactorer import CyclomaticComplexityRefactorer

class TestComplexityRefactorer(unittest.TestCase):
    def setUp(self):
        self.refactorer = CyclomaticComplexityRefactorer(max_allowed_complexity=3)

    def test_simple_function(self):
        code = "def simple(a): return a * 2"
        reps = self.refactorer.analyze_source(code)
        self.assertEqual(len(reps), 1)
        self.assertEqual(reps[0].complexity, 1)
        self.assertFalse(reps[0].needs_refactor)

    def test_complex_function(self):
        code = """def complex_fn(a, b, c):
    if a:
        for x in b:
            if c:
                pass"""
        reps = self.refactorer.analyze_source(code)
        self.assertEqual(len(reps), 1)
        self.assertGreater(reps[0].complexity, 3)
        self.assertTrue(reps[0].needs_refactor)

if __name__ == "__main__":
    unittest.main()
