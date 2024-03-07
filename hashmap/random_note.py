def can_construct(ransomNote, magazine):
    from collections import Counter
    return not Counter(ransomNote) - Counter(magazine)


print(can_construct("a", "b"))  
print(can_construct("aa", "ab")) 
print(can_construct("aa", "aab")) 