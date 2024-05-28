def uniquePaths(self, m: int, n: int) -> int:
        total=0
        dp=[['.' for j in range(n+1)] for i in range(m+1)]
        def dynamicprog(i,j ,total,dp):
            if i==m-1 and j==n-1:
                total+=1
                return total
            elif i>=m or j>=n:
                return 0
            else:
                if dp[i+1][j]=='.' and dp[i][j+1]=='.':
                    return dynamicprog(i+1,j,total,dp)+dynamicprog(i,j+1,total,dp)
                elif  dp[i+1][j]!='.' and dp[i][j+1]=='.':
                    dp[i+1][j]=dynamicprog(i,j+1,total,dp)
                    return dp[i+1][j]+dp[i][j+1]
                elif  dp[i+1][j]=='.' and dp[i][j+1]!='.':
                    dp[i][j+1]=dynamicprog(i,j+1,total,dp)
                    return dp[i+1][j]+dp[i][j+1]
                else:
                    return dp[i+1][j]+dp[i][j+1]
        print(dynamicprog(0,0,total,dp))
        return dynamicprog(0,0,total,dp)
