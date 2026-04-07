class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let set= new Map();
        for(let i=0;i<nums.length;i++){
            if(set.get(nums[i])){
                return true;
            }
            else{
                set.set(nums[i],i+1);
            }
        }
        return false;
    }
}
