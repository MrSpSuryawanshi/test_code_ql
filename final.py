from pylint.lint import Run
files_to_lint = ['app.py','app2.py']  # Replace with the path to your Python file
results = Run(["--rcfile=.pylintrc"] + files_to_lint, exit=False)
