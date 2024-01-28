class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        d = dict()
        maxy = -1
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i in range(len(nums)-1,-1,-1):
            cnt = 0
            comp = math.sqrt(nums[i])
            while(int(comp)!=1 and math.floor(comp) == math.ceil(comp) and int(comp) in d and d[int(comp)]>=2):
                cnt += 1;
                comp = math.sqrt(comp)
            maxy = 2*cnt+1 if (2*cnt+1)>maxy else maxy
        ones = d[1] if 1 in d else 0 
        ones = ones-1 if ones %2 == 0 else ones
        return maxy if maxy > (ones) else ones
            
        
        