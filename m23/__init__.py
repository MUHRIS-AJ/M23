"""
M23 Language Package
===================
Human-friendly, English-like data science programming language.
"""

# Try to import interpreter and runtime modules safely
try:
    # When run as a standalone script (for testing)
    import interpreter
    import runtime
except ImportError:
    # When used as a proper package
    from . import interpreter
    from . import runtime

# Optional: define a main function to run scripts from package
def main():
    """
    Entry point for running an M23 script from the command line:
    python -m m23 <script.m23>
    or
    m23 <script.m23>  # via console script
    """
    import sys
    if len(sys.argv) < 2:
        print("Usage: m23 <file.m23>")
        sys.exit(1)

    script_file = sys.argv[1]
    try:
        interpreter.run_m23(script_file)  # Call the main function in interpreter.py
    except AttributeError:
        print("[ERROR] interpreter.py must have a function 'run_m23(file)' to execute scripts.")
        sys.exit(1)
