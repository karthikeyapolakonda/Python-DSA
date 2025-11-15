Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

brackets = {')' : '(', ']' : '[', '}' : '{'}
s = '([])'
stack = []
flag = 0
for char in s:
    if char in brackets:
        if not stack or stack[-1] != brackets[char]:
            print('false')
            flag = 1
            break
        stack.pop()
    else:
        stack.append(char)
if not stack and flag == 0:
    print('true')
