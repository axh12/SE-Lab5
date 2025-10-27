1. Which issues were the easiest to fix, and which were the hardest? Why?
Easiest:
Formatting fixes: Adding final newlines, fixing blank line spacing
Syntax updates: Converting % formatting to f-strings
Simple cleanup: Removing unused imports

Why: These were mechanical changes following clear style rules

Hardest:
Input validation: Adding type checks for all function parameters
Exception handling: Replacing bare except: with specific exception types
Error recovery: Ensuring graceful failure without crashes

Why: Required deep understanding of code functionality and potential edge cases

2. Did the static analysis tools report any false positives? If so, describe one example.
Yes - The global variable (stock_data) was flagged as a code quality issue. While global state is generally discouraged in large applications, for this simple inventory system with a single data store, it was an acceptable design choice. The tools couldn't understand the appropriate context and scale.

3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
Local Development:
Pre-commit hooks to run analysis before each commit
IDE plugins for real-time feedback while coding
Makefile commands for quick linting (make lint, make security-check)

CI/CD Pipeline:
Automated static analysis on every pull request
Quality gates blocking merges with critical issues
Scheduled security scans of the entire codebase
Progressive enforcement from warnings to required fixes

Team Practices:
Static analysis results as part of code review criteria
Regular team training on interpreting tool outputs
Quality metrics tracking over time

4. What tangible improvements did you observe in the code quality, readability, or potential
robustness after applying the fixes?
Local Development:
Pre-commit hooks to run analysis before each commit
IDE plugins for real-time feedback while coding
Makefile commands for quick linting (make lint, make security-check)

CI/CD Pipeline:
Automated static analysis on every pull request
Quality gates blocking merges with critical issues
Scheduled security scans of the entire codebase
Progressive enforcement from warnings to required fixes

Team Practices:
Static analysis results as part of code review criteria
Regular team training on interpreting tool outputs
Quality metrics tracking over time