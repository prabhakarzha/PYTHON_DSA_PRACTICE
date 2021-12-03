value = int(input("enter value"))
def maxProfit(price, n, k):

    profit = [[0 for i in range(n + 1)]
                 for j in range(k + 1)]
 
    for i in range(1, k + 1):
        prevDiff = float('-inf')
         
        for j in range(1, n):
            prevDiff = max(prevDiff,
                           profit[i - 1][j - 1] -
                           price[j - 1])
            profit[i][j] = max(profit[i][j - 1],
                               price[j] + prevDiff)
 
    return profit[k][n - 1]
 
# Driver Code
if __name__ == "__main__":
 
    k = 2
    price = [12, 5]
    n = len(price)
 
    print("Maximum profit is:",
           maxProfit(price, n, k))