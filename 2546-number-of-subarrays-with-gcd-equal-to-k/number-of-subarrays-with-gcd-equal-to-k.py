class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i,len(nums)):
                curr = gcd(nums[j],curr)
                if gcd(nums[j],curr)==k:
                    count += 1
        return count
                    
                
        