class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map=new Map();
        let frequency=[];
        let ans=[]
        for(let i=0;i<nums.length;i++){
            if(map.get(nums[i])){
                map.set(nums[i],map.get(nums[i])+1)
            }
            else{
                map.set(nums[i],1)
            }
        }
        frequency = Array.from(map.entries());
        frequency.sort((a, b) => b[1] - a[1]);
        ans=frequency.slice(0,k).map(entry => entry[0])
        //console.log(ans)
        return ans;

    }
}
