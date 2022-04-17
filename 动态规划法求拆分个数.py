import numpy as np
def Split(n,k):
	dp = np.zeros((n+1,k+1))
	# 动态规划实现整数拆分
	for i in range (1,n+1):
		for j in range(1,k+1):
			if i ==1 and j ==1:
				dp[i,j]=1
			elif i<j:
				dp[i,j]=dp[i,i]
			elif i == j:
				dp[i,j] = dp[i,j-1]+1
			else:
				dp[i,j]=dp[i,j-1]+dp[i-j,j]
	#print(dp)
	return dp[-1,-1]
count = Split(5,5)
print('拆分方案个数为：',int(count))