
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
