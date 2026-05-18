class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    helper(c) {
        const lower = 'a'.charCodeAt(0) <= c.charCodeAt(0) &&
            c.charCodeAt(0) <= 'z'.charCodeAt(0),
            upper = 'A'.charCodeAt(0) <= c.charCodeAt(0) &&
            c.charCodeAt(0) <= 'Z'.charCodeAt(0),
            number = '0'.charCodeAt(0) <= c.charCodeAt(0) &&
            c.charCodeAt(0) <= '9'.charCodeAt(0);
        return lower || upper || number;
    }

    isPalindrome(s) {

        let l = 0,
            r = s.length - 1;

        while (l < r) {
            while (l < r && !this.helper(s[l])) {
                l++;
            }

            while (l < r && !this.helper(s[r])) {
                r--;
            }
            console.log(s[l].toLowerCase(), s[r].toLowerCase())
            if (s[l].toLowerCase() != s[r].toLowerCase()) {
                return false;
            }

            l++;
            r--;
        }
        return true;
    }
}
