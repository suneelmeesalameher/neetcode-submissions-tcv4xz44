class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let ans=0;
        let l=0;
        let r=height.length-1
        let maxL=height[0];
        let maxR=height[height.length-1]
        //for(let i=0;i<height.length;i++){
        while(l<r){
            if(maxL<maxR){
                l+=1
                maxL=Math.max(maxL,height[l]);
                ans+=maxL-height[l];
                // if(sum>0){
                //     ans+=sum
                // }
                // if(height[l]>maxL){
                //     maxL=height[l]
                // }
                
            }
            else{
                r-=1
                maxR=Math.max(maxR, height[r]);
                ans+=maxR-height[r]
                // if(sum>0){
                //     ans+=sum
                // }
                // if(height[r]>maxR){
                //     maxR=height[r]
                // }
                
            }
        }
        return ans
    }
}
