#Question 3
def maxProfit(prices):
  max_profit = 0
  temp = prices[0]
  for i in range(1,len(prices)):
    profit = prices[i]-temp
    max_profit = max(max_profit,profit)
    if profit<0:
      temp = prices[i]
  return max_profit
print(maxProfit([7,6,4,3,1]))