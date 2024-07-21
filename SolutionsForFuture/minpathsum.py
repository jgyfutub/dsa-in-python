class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) 
        n = len(grid[0]) 
        memo = {}
        def top_down(x, y, cur_sum = 0):
            # print(f"{x}, {y}, {cur_sum}, {grid[x][y]}")
            if x == m-1 and y == n-1:
                return cur_sum + grid[x][y]
            ans = -1
            if (x,y) in memo:
                return memo[(x,y)] + cur_sum
            elif x + 1 < m and y+1 < n:
                ans = min(top_down(x+1,y, cur_sum + grid[x][y]) , 
                top_down(x,y+1, cur_sum + grid[x][y]))
            elif x+1 < m:
                ans = top_down(x+1, y, cur_sum + grid[x][y]) 
            elif y+1 < n:
                ans = top_down(x, y+1, cur_sum + grid[x][y]) 
            memo[(x,y)] = ans - cur_sum
            return ans
        
        def bottom_up():
            dp = [[ math.inf] * n for i in range(m)]
            dp[0][0] = grid[0][0]
            for i in range(1,n):
                dp[0][i] = dp[0][i-1] + grid[0][i]

            for i in range(1,m):
                for j in range(0,n):
                    if j-1 >= 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                    else:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
            return dp[m-1][n-1]


        return bottom_up()
        return top_down(0 , 0)
        
