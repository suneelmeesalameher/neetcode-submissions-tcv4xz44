class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map=new Map();
        for(let i=0; i<nums.length;i++){
            map.set(nums[i],i);
        }
        for(let i=0;i<nums.length;i++){
            if(map.get(target-nums[i])){
                let x=map.get(target-nums[i]);
                    if(x!=i){
                    console.log(x);
                    return [x,i];
                    }
            }
        }
        return [];
    }
}
