class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xorAll = 0
        for i in range(1,len(nums)+1):
            xorAll = xorAll ^ i
        for i in range(len(nums)):
            xorAll ^= nums[i]
        resultXor = xorAll & -xorAll
        xorSet,xorNotSet = 0, 0
        for i in range(1,len(nums)+1):
            if (resultXor & i):
                xorSet ^= i
            else:
                xorNotSet ^= i
        for i in range(len(nums)):
            if ((resultXor & nums[i])):
                xorSet ^= nums[i]
            else:
                xorNotSet ^= nums[i]
        return [xorSet,xorNotSet] if xorNotSet not in nums else [xorNotSet,xorSet]