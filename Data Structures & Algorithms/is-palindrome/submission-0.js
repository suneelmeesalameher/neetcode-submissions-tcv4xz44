class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let arr=s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
        let revarr=arr.split('').reverse().join('');
        if(arr===revarr){
            return true;
        }
        else{
            return false;
        }
    }
}
