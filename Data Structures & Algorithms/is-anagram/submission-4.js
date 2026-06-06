class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
        
        const countS = {}
        for(const c of s) {
            countS[c] = (countS[c] || 0) + 1
        }

        const countT = {}
        for(const c of t) {
            countT[c] = (countT[c] || 0) + 1
        }
    
    if (countS.length !== countT.length) return false

    for (const key in countS) {
        if (countS[key] !== countT[key]) return false
    }
    return true
    }

    
}
