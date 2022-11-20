def isSafe(arr,x,y,n):
    for row in range(x):
        if arr[row][y]==1:
            return False
    row=x
    col=y
    while (row>=0 and col>=0):
        if arr[row][col]==1:
            return False
        row=row-1
        col=col-1
    row=x
    col=y
    while (row>=0 and col<n):
        if arr[row][col]==1:
            return False
        row=row-1
        col=col+1
    return True

def printBoard(arr,n):
    global count
    count=count+1
    print(count)
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                print("[Q]",end=" ")
            else:
                print("[]",end=" ")
        print()
    print()
    print()

def nQueen(arr,x,n):
    if(x==n):
        printBoard(arr,n)
        return
    for col in range(n):
        if isSafe(arr,x,col,n):
            arr[x][col]=1
            nQueen(arr,x+1,n)
            arr[x][col]=0

count=0
n=int(input("Enter no.: "))
#n=4
arr = [[0 for i in range(n)] for j in range(n)]
nQueen(arr,0,n)

