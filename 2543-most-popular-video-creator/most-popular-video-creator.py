class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        maxSum = dict()
        maxval = dict()
        maxID = dict()
        for i in range(len(creators)):
            if  creators[i] not in maxSum:
                maxSum[creators[i]] = views[i]
                maxval[creators[i]] = views[i]
                maxID[creators[i]] = ids[i]
            else:
                maxSum[creators[i]] += views[i]
                if views[i] == maxval[creators[i]]:
                    maxID[creators[i]] = ids[i] if maxID[creators[i]] > ids[i] else maxID[creators[i]]
                if views[i] > maxval[creators[i]]:
                    maxval[creators[i]] = views[i]
                    maxID[creators[i]] = ids[i]
        maxval = max(maxSum.values())
        maxkeys = [key for key,value in maxSum.items() if value == maxval]
        result =[]
        for i in maxkeys:
            result.append([i,maxID[i]])
        return result
                    
        
        
        