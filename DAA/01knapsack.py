def knapSack(W, wt, val, n):
	K=[[0 for x in range(W + 1)] for x in range(n + 1)]
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:   #this one is assuming ki weight array mein starting also has 0 in it
				K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
			else:
				K[i][w] = K[i-1][w] 
	return K[n][W]


# Driver code
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
val=[]
wt=[]
W=int(input("enter total Weight : "))
n=int(input("No of items"))
print("Enter weight and value of items ")
for i in range(0,n):
    w=int(input("weight: "))
    v=int(input("value: "))
    val.append(v)
    wt.append(w)
print(knapSack(W, wt, val, n))


