w = [92 ,4 ,43 ,83 ,84 ,68 ,92 ,82 ,6 ,44 ,32 ,18 ,56 ,83 ,25 ,96 ,70 ,48 ,14 ,58]
v = [44 ,46 ,90 ,72 ,91, 40 ,75 ,35 ,8 ,54 ,78 ,40 ,77 ,15 ,61 ,17 ,75 ,29 ,75 ,63]
import numpy as np
C = 878
def KnapSack(w,v,C):
	n = len(w)
	x = [i for i in range(n)]
	#求出Value矩阵
	V = np.zeros((n+1,C+1)) # V : 0~n 0~C
	for i in range(1,n+1):
		for j in range(1,C+1):
			if j<w[i-1]:
				V[i,j] = V[i-1,j]
			else:
				V[i,j]=max(V[i-1,j],V[i-1,j-w[i-1]]+v[i-1])
	# 求出最优解
	for i in range(n,-1,-1):
		if V[i,j]>V[i-1,j]:
			x[i-1]=1
			j=j-w[i-1]
		else:
			x[i-1]=0
	return V[n,C],x #返回最大价值

Max,x = KnapSack(w,v,C) 
print('背包取得的最大价值为：',Max)
print('问题的最优解为：',x)

