def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()

    return result + sign * num

# Example usage
s1 = "1 + 1"
print(calculate(s1))  # Output: 2

s2 = " 2-1 + 2 "
print(calculate(s2))  # Output: 3

s3 = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s3))  # Output: 23