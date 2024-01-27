class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        
        @cache
        def traverse(startrow,startcol,maxmove):
            if startrow<0 or startrow>m-1 or startcol<0 or startcol>n-1:
                return 1
            if maxmove == 0:
                return 0
            cnt=0
            for i in range(4):
                cnt = (cnt + traverse(startrow+directions[i][0],startcol+directions[i][1],maxmove-1))%(10**9+7)
            return cnt
        return traverse(startRow,startColumn,maxMove)

        