class Solution:
    def encode(self, strs: List[str]) -> str:
        word=""
        for s in strs:
            word=word+str(len(s))+'#'+s
        return word



    def decode(self, s: str) -> List[str]:
        words=[]
        i=0
        while i<len(s):
            num=0
            while s[i].isdigit():
                num=num*10+int(s[i])
                i+=1

            i+=1
            words.append(s[i:i+num])
            i+=num
        return words