class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let set=new Set(nums);
        let count=0;
        for(let value of set){
            if(!set.has(value-1)){
                let length=1;
                while(set.has(value+length)){
                   length++; 
                }
                count=Math.max(length,count);
            }
        }
        return count
    }
}
