class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let num_set = new Set();
        for(let num of nums){
            if(num_set.has(num)) return true;
            num_set.add(num);
        }
        return false;
    }
}
