def findMinCost(twoDArray,row,col):
    if row ==-1 or col==-1:
        return float('inf')
    elif row==0 and col==0:
        return twoDArray[0][0]
    else:
        op1=findMinCost(twoDArray,row-1,col)
        op2=findMinCost(twoDArray,row,col-1)
        return twoDArray[row][col]+min(op1,op2)