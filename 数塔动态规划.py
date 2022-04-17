import numpy as np
import time
a = np.random.randint(low=1,high=100,size=(20,20),dtype='int')
# print(a,a.shape)
tower = np.tril(a)
print(tower)
def datatower(tower,n): # 动态规划法
	maxAdd = np.zeros((n,n))
	path = np.zeros((n,n))
	for j in range(n):
		maxAdd[n-1,j] = tower[n-1,j] # 初始化最底层，也就是tower的最底层
		#print(maxAdd)

	for i in range(n-2,-1,-1):
		#print(i)
		for j in range(0,i+1):
			if maxAdd[i+1,j]>maxAdd[i+1,j+1]:
				maxAdd[i,j] = tower[i,j]+maxAdd[i+1,j]
				path[i,j] = j
			else:
				maxAdd[i,j] = tower[i,j]+maxAdd[i+1,j+1]
				path[i,j] = j+1
			#print('i is:',i,maxAdd[i,j])
	print("the path is:",tower[0,0],end='')
	#print(path)
	j = int(path[0,0])
	for i in range(1,n):
		print(f"-->{tower[i,j]}",end='')
		j = int(path[i,j])
	#print(maxAdd)
	return maxAdd[0,0]

tic1 = time.perf_counter()
Max = datatower(tower,20)
print('\nMax = ',Max)
toc1 = time.perf_counter()
shijian1 = toc1-tic1
print('动态规划法时间消耗：',shijian1)

# 枚举法：
Sum = 0
Max_2 = 0
tic2 = time.perf_counter()
for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					for f in range(2):
						for g in range(2):
							for h in range(2):
								for i in range(2):
									#print(i)
									for j in range(2):
										for k in range(2):
											for l in range(2):
												for m in range(2):
													for n in range(2):
														for o in range(2):
															for p in range(2):
																for q in range(2):
																	for r in range(2):
																		for s in range(2):
																			#A = np.array([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t])
																			Sum = tower[0,0]+tower[1,0+a]+tower[2,0+a+b]+tower[3,0+a+b+c]\
																				+tower[4,0+a+b+c+d]+tower[5,0+a+b+c+d+e]+tower[6,0+a+b+c+d+e+f]+tower[7,0+a+b+c+d+e+f+g]\
																				+tower[8,0+a+b+c+d+e+f+g+h]+tower[9,0+a+b+c+d+e+f+g+h+i]+tower[10,0+a+b+c+d+e+f+g+h+i+j]+tower[11,0+a+b+c+d+e+f+g+h+i+j+k]\
																				+tower[12,0+a+b+c+d+e+f+g+h+i+j+k+l]+tower[13,0+a+b+c+d+e+f+g+h+i+j+k+l+m]+tower[14,0+a+b+c+d+e+f+g+h+i+j+k+l+m+n]+tower[15,0+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o]\
																				+tower[16,0+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p]+tower[17,0+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q]+tower[18,0+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r]+tower[19,0+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s]
																			if Sum>Max_2:
																				Max_2 = Sum

toc2 = time.perf_counter()
shijian2 = toc2-tic2
print("Max =",Max_2)
print('蛮力法时间消耗',shijian2)
