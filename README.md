Task: Given a string containing a mixture of parentheses (‘(’, ‘)’, ‘{’, ‘}’, ‘[’, ‘]’), write a function to determine
if the input string is valid.
A valid string is one where all parentheses are closed in the correct order. For example:

"()", "[()]", "{([])}" are valid strings.

"{[}]", "(]", "[(])" are invalid strings.

Requirements:

Write a Python function is_valid_parentheses that takes a string containing parentheses as input and returns True if
the parentheses are valid, False otherwise.

The function should handle other characters gracefully and ignore them.

Optimize the solution for time complexity. Aim for O(n) or better if possible.

Bonus:

Modify the function to return the indices of mismatched parentheses if the string is invalid.

Write unit tests to verify the correctness of the function.

