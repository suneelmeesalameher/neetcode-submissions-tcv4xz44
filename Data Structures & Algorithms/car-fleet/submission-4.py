class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        carfleet=1
        for i in range(0, len(position)):
            stack.append((position[i],speed[i]))
        stack.sort()
        if len(stack)==1:
            return 1
        #print(stack)
        (ref_pos, ref_speed)= stack.pop()
        ref_time = float((target-ref_pos)/ref_speed)
        while stack:
            cur_pos, cur_speed= stack.pop()
            cur_time= float((target-cur_pos)/cur_speed)
            if (cur_time>ref_time):
                carfleet+=1
                ref_pos , ref_speed , ref_time = cur_pos, cur_speed, cur_time
        return carfleet





        
