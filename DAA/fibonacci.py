def iterativeFibbonacci(n):
    f=[]
    f.append(0)
    f.append(1)
    cnt=2
    for i in range(2,n):
        cnt=cnt+1
        f.append(f[i-1]+f[i-2])
    return cnt

def recursiveFibbonacci(n):
    global rSteps
    rSteps=rSteps+1
    if n<=1:
        return n
    return recursiveFibbonacci(n-1)+recursiveFibbonacci(n-2)


rSteps = 0
n=int(input("Enter n: "))
print("Fibbonacci Value : ",recursiveFibbonacci(n))
print("Steps required using Iteration : ",iterativeFibbonacci(n))
print("Steps required using recursion : ",rSteps)
