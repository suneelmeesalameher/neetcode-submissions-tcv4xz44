class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let s1= new Map();
        let s2= new Map();
        let s1Length=s.length;
        let s2Length = t.length;
        if(s1Length!==s2Length){
            return false;
        }
        for(let i=0; i<s1Length;i++){
            if(s1.get(s[i])){
                s1.set(s[i],s1.get(s[i])+1);
            }
            else{
                s1.set(s[i],1);
            }
        }
        for(let i=0; i<s2Length;i++){
            if(s1.get(t[i])){
                s1.set(t[i],s1.get(t[i])-1);
            }
            else{
                return false;
            }
        }
        for(let i=0; i<s1Length;i++){
            if(s1.get(s[i])>0){
                return false;
            }
        }
        return true;


    }
}
