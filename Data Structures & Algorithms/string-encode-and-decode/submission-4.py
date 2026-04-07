class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for x in strs:
            s=s+str(len(x))
            s=s+'#'
            s=s+x
        return s;

    def decode(self, s: str) -> List[str]:
        l=[]
        st=""
        x=0
        while x<len(s):
            j= s.find('#', x)
            length = int(s[x:j])
            x = j + 1 
            l.append(s[x:x + length])
            x += length 
        return l
