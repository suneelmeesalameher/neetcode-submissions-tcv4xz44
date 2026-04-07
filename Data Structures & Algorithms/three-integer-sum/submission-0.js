class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let arr=nums.sort((a, b) => a - b)
        //console.log("arr",arr)
        let ans=[]
        for (let i = 0; i < arr.length; i++) {
        // Skip duplicate values for the first element
        if (i > 0 && arr[i] === arr[i - 1]) continue;
            //let a=arr[i]
            let front=i+1
            let back=arr.length-1
            while(front<back){
                //if (i > 0 && arr[i] === arr[i - 1]) continue;
                    //console.log("arr[i]",arr[i])
                    //console.log("arr[front]",arr[front])
                    //console.log("arr[back]",arr[back])
                    let sum=arr[front]+arr[back]+arr[i];
                    //console.log("sum",sum)
                    if(sum==0){
                        ans.push([arr[i],arr[front],arr[back]])
                        front+=1
                        back--;
                        while (front < back && arr[front] === arr[front - 1]) front++;
                while (front < back && arr[back] === arr[back + 1]) back--;
                    }
                    if(sum>0){
                        back=back-1;
                    }
                    if(sum<0){
                        front=front+1
                    }
                }
        }
        console.log("ans",ans)
        return ans;
    }
}
