class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hashDiff = {}
        
        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i]
            
            if (diff in hashDiff) return [ hashDiff[diff], i ]
            
            hashDiff[nums[i]] = i
        }
        
    }
}
