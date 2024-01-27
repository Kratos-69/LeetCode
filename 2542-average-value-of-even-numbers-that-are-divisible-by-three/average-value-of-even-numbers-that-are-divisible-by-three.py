class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sums,cnt = 0,0
        for i in nums:
            if i%3==0 and i%2==0:
                sums += i
                cnt += 1
        return sums//cnt if cnt>0 else 0
        