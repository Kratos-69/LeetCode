class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt,prev,nexs,sums =0,0,0,0
        d=dict()
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0)+1
        for i in d:
            sums += d[i]
        for i in d:
            nexs = sums-prev-d[i]
            cnt += prev*d[i]*nexs
            prev += d[i]
        return cnt
