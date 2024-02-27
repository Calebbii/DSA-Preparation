def simplify_path(path):
    stack = []
    elements = path.split('/')
    
    for element in elements:
        if element == '..':
            if stack:
                stack.pop()
        elif element and element != '.':
            stack.append(element)
    
    return '/' + '/'.join(stack)

# Test the function
path1 = "/home/"
print(simplify_path(path1))  # Output: "/home"

path2 = "/../"
print(simplify_path(path2))  # Output: "/"

path3 = "/home//foo/"
print(simplify_path(path3))  # Output: "/home/foo"