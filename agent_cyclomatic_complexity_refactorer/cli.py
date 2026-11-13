"""CLI for agent-cyclomatic-complexity-refactorer."""
import sys
import argparse
from .refactorer import CyclomaticComplexityRefactorer

def main():
    parser = argparse.ArgumentParser(description="Agent Cyclomatic Complexity Refactorer CLI")
    parser.add_argument("--demo", action="store_true", help="Run cyclomatic complexity analysis demo")
    args = parser.parse_args()

    if args.demo:
        refactorer = CyclomaticComplexityRefactorer(max_allowed_complexity=3)
        code = """def process_order(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                return x + y + z
    return 0"""
        reports = refactorer.analyze_source(code)
        for r in reports:
            print(f"[+] Function '{r.function_name}': complexity={r.complexity}, needs_refactor={r.needs_refactor}")
            for s in r.suggestions:
                print(f"    - {s}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
