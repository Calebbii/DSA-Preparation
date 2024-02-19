def removeduplicate(numbers):
    sorted =[]
    for n in numbers:
        if n not in sorted:
            sorted.append(n)
        
    return f'Output: k={len(sorted)}, nums ={sorted}'

print (removeduplicate([1,1,1,6,1,1,2,3,1,1]))
