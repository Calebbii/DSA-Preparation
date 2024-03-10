function isIsomorphic(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const sToT = new Map();
    const tToS = new Map();

    for (let i = 0; i < s.length; i++) {
        const charS = s[i];
        const charT = t[i];

        if (sToT.has(charS) && sToT.get(charS) !== charT) {
            return false;
        }

        if (tToS.has(charT) && tToS.get(charT) !== charS) {
            return false;
        }

        sToT.set(charS, charT);
        tToS.set(charT, charS);
    }

    return true;
}

// Test cases

console.log(isIsomorphic("egg", "add"));     // Output: true
console.log(isIsomorphic("foo", "bar"));     // Output: false
console.log(isIsomorphic("paper", "title")); // Output: true