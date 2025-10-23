"""
M23 Language Package
===================
Human-friendly, English-like data science programming language.
"""

# Try to import interpreter and runtime modules safely
try:
    import interpreter
    import runtime
except ImportError:
    # If using as a package (relative imports)
    from . import interpreter
    from . import runtime

# Optional: define a main function to run scripts from package
def main():
    """
    Entry point for running an M23 script from the command line:
    python -m m23 <script.m23>
    """
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m m23 <file.m23>")
    else:
        script = sys.argv[1]
        interpreter.main(script)  # Updated to call main() in interpreter
