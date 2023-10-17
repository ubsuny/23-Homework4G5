                              # Documentation for the project/ Github action.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production
GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.
There are different components in the github action, 
#The components of GitHub Actions
You can configure a GitHub Actions workflow to be triggered when an event occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more jobs which can run in sequential order or in parallel. Each job will run inside its own virtual machine runner, or inside a container, and has one or more steps that either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.
<img width="682" alt="Screenshot 2023-10-13 at 5 34 06 PM" src="https://github.com/ubsuny/23-Homework4G5/assets/13534352/3143d8c1-3279-451a-a458-907215eced8b">








# Unit Test Result Using pytest
============================= test session starts ==============================  
          
          platform linux -- Python 3.8.18, pytest-7.4.2, pluggy-1.3.0  
          rootdir: /home/runner/work/23-Homework4G5/23-Homework4G5  
          collected 3 items  
          pytest_matrix_multiply.py ...                         [100%]  

============================== 3 passed in 0.13s ===============================

The above result indicates that 
- the testing was performed on a Linux platform using Python 3.8.18 with pytest version 7.4.2.
- the rootdir specifies the directory where our tests were run.
- collected 3 items indicates that pytest found and ran 3 test functions or methods.
- pytest_matrix_multiply.py ... shows that all three tests in the file pytest_matrix_multiply.py passed 
    Note: (each . represents a passed test).
- The summary 3 passed in 0.13s confirms that all 3 tests were successful and they ran in 0.13 seconds.

So, it appears that pytest worked correctly, and all our tests passed successfully.

# Unit Test Result Using pylint

************* Module pytest_matrix_multiply  
pytest_matrix_multiply.py:30:44: C0303: Trailing whitespace (trailing-whitespace)  
pytest_matrix_multiply.py:64:0: C0301: Line too long (111/100) (line-too-long)  
pytest_matrix_multiply.py:97:0: C0305: Trailing newlines (trailing-newlines)  
pytest_matrix_multiply.py:1:0: C0114: Missing module docstring (missing-module-docstring)  
pytest_matrix_multiply.py:15:27: C0103: Argument name "A" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:15:30: C0103: Argument name "B" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:15:27: W0621: Redefining name 'A' from outer scope (line 11) (redefined-outer-name)  
pytest_matrix_multiply.py:15:30: W0621: Redefining name 'B' from outer scope (line 12) (redefined-outer-name)  
pytest_matrix_multiply.py:26:4: C0103: Variable name "C" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:34:23: C0103: Argument name "A" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:34:26: C0103: Argument name "B" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:34:23: W0621: Redefining name 'A' from outer scope (line 11) (redefined-outer-name)  
pytest_matrix_multiply.py:34:26: W0621: Redefining name 'B' from outer scope (line 12) (redefined-outer-name)  
pytest_matrix_multiply.py:48:27: C0103: Argument name "A" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:48:30: C0103: Argument name "B" doesn't conform to snake_case naming style (invalid-name)  
pytest_matrix_multiply.py:48:27: W0621: Redefining name 'A' from outer scope (line 11) (redefined-outer-name)  
pytest_matrix_multiply.py:48:30: W0621: Redefining name 'B' from outer scope (line 12) (redefined-outer-name)  
pytest_matrix_multiply.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)  
pytest_matrix_multiply.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)  
pytest_matrix_multiply.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)  
pytest_matrix_multiply.py:3:0: C0411: standard import "import time" should be placed before "import numpy as np" (wrong-import-order)  

-----------------------------------
Your code has been rated at 5.12/10

-----------------------------------

The necessary changes are
- Remove any trailing whitespace.
- Ensure no lines are longer than 100 characters.
- Remove any trailing newlines.
- Add a module docstring.
- Replace the variable names "A", "B", and "C" with snake_case names.
- Reorder the imports.
- Add docstrings to the test functions.
 
 After making these changes, we got
 
------------------------------------
Your code has been rated at 10.00/10

-----------------------------------
