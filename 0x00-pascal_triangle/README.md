
---

# Pascal's Triangle

## Project Overview

This project focuses on generating Pascal's Triangle using Python. Pascal's Triangle is a triangular array of binomial coefficients. This project is a part of the ALX curriculum, under the Python specialization. You will create a function that returns a list of lists of integers representing Pascal's Triangle up to a given number of rows.

## Project Timeline

- **Project Start:** Jun 24, 2024, 11:00 AM
- **Project End:** Jun 28, 2024, 11:00 AM
- **Checker Release:** Jun 25, 2024, 11:00 AM
- **Auto Review:** Launched at the deadline

## Resources

To understand and complete this project, you may find the following resources helpful:

- [What is Pascal’s Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=XMriWTvPXHI)
- [What are Python Algorithms](https://www.geeksforgeeks.org/python-algorithm/)

## Additional Resources

- **Mock Technical Interview**
- **Must Know Python Concepts:**
  - **Lists and List Comprehensions**
  - **Functions**
  - **Loops**
  - **Conditional Statements**
  - **Recursion (Optional)**
  - **Arithmetic Operations**
  - **Indexing and Slicing**
  - **Memory Management**
  - **Error and Exception Handling (Optional)**
  - **Efficiency and Optimization**

## Key Python Concepts

To successfully complete this project, revise the following Python concepts:

### Lists and List Comprehensions
- Create, access, modify, and iterate over lists.
- Utilize list comprehensions for concise and readable code.

### Functions
- Define and call functions.
- Pass parameters and return values, particularly lists of lists.

### Loops
- Use `for` and `while` loops to iterate through sequences.
- Utilize nested loops for generating each row of Pascal's Triangle.

### Conditional Statements
- Implement `if`, `elif`, and `else` conditions for logic based on position within Pascal's Triangle.

### Recursion (Optional)
- Understand recursion for an alternative approach to generating Pascal's Triangle.

### Arithmetic Operations
- Perform addition to calculate each element as the sum of the two elements directly above it.

### Indexing and Slicing
- Access elements and slices of lists to construct each row of the triangle.

### Memory Management
- Be mindful of how lists are stored and copied.

### Error and Exception Handling (Optional)
- Use `try-except` blocks to handle potential errors.

### Efficiency and Optimization
- Consider time and space complexity.
- Apply optimizations to improve performance.

## Task

### Pascal's Triangle
- **Objective:** Create a function `def pascal_triangle(n):` that returns a list of lists representing Pascal's Triangle of `n`.
- **Requirements:**
  - Returns an empty list if `n <= 0`.
  - Assumes `n` will always be an integer.

### Example Usage

```python
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$
```

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/Wambuuyy/alx-interview)
- **Directory:** `0x00-pascal_triangle`
- **File:** `0-pascal_triangle.py`

---

© 2024 ALX, All rights reserved.