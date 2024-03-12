function wordPattern(pattern, s) {
    const words = s.split(' ');
    
    if (pattern.length !== words.length) {
        return false;
    }
    
    const charToWord = new Map();
    const wordToChar = new Map();
    
    for (let i = 0; i < pattern.length; i++) {
        const char = pattern[i];
        const word = words[i];
        
        if (charToWord.has(char)) {
            if (charToWord.get(char) !== word) {
                return false;
            }
        } else {
            charToWord.set(char, word);
        }
        
        if (wordToChar.has(word)) {
            if (wordToChar.get(word) !== char) {
                return false;
            }
        } else {
            wordToChar.set(word, char);
        }
    }
    
    return true;
}

console.log(wordPattern("abba", "dog cat cat dog"));  // Output: true
console.log(wordPattern("abba", "dog cat cat fish"));  // Output: false
console.log(wordPattern("aaaa", "dog cat cat dog"));  // Output: false