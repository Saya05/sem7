class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

def fractionalKnapsack(W, arr):
	arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
	finalvalue = 0.0
	for item in arr:
		if item.weight <= W:
			W=W-item.weight
			finalvalue=finalvalue+item.value
		else:
			finalvalue=finalvalue+ item.value*W/item.weight
			break	
	return finalvalue



arr=[]
W=int(input("enter total Weight : "))
n=int(input("No of items"))
print("Enter value and weight of items ")
for i in range(0,n):
	v=int(input("Value: "))
	w=int(input("Weight: "))
	arr.append(Item(v,w))
#W = 50
#arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
max_val = fractionalKnapsack(W, arr)
print(max_val)
