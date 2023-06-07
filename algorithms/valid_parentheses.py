"""
Leetcode Question: https://leetcode.com/problems/valid-parentheses/
"""


def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            c1 = stack.pop()
            if c1 == '{' and c != '}':
                return False
            if c1 == '[' and c != ']':
                return False
            if c1 == '(' and c != ')':
                return False
    return not stack


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
