var lengthOfLongestSubstring = function(s) {
    let maxLength = 0;
    let start = 0;
    let charIndexMap = {};

    for (let i = 0; i < s.length; i++) {
        if (s[i] in charIndexMap) {
            start = Math.max(start, charIndexMap[s[i]] + 1);
        }
        charIndexMap[s[i]] = i;
        maxLength = Math.max(maxLength, i - start + 1);
    }

    return maxLength;
};