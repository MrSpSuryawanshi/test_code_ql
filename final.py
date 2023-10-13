from pylint.lint import Run
files_to_lint = ['your_python_scripts.py']  # Replace with the path to your Python file
results = Run(["--rcfile=.pylintrc"] + files_to_lint, exit=False)
