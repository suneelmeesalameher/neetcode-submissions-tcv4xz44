class Solution:
    def encode(self, strs: List[str]) -> str:
        words=""
        for s in strs:
            words+=str(len(s))+"#"+s
        return words




    def decode(self, s: str) -> List[str]:
        l=[]
        left=0
        while left<len(s):
            j=s.find('#',left)
            length = int(s[left:j])
            left=j+1
            l.append(s[left: left+length])
            left+=length
        return l
        