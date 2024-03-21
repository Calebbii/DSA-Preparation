def minWindow(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    target_counts = Counter(t)
    required = len(target_counts)
    formed = 0
    window_counts = {}
    
    left, right = 0, 0
    ans = float('inf'), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1
        
        while formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right + 1)
            
            char = s[left]
            window_counts[char] -= 1
            if char in target_counts and window_counts[char] < target_counts[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]]

print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(minWindow("a", "a"))  # Output: "a"
print(minWindow("a", "aa"))  # Output: ""