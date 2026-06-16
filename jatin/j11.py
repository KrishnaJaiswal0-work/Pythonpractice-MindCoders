import numpy as np 

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print()
print(np.mean(arr))
print()
print(np.mean(arr,axis = 0))  # coloumn wise 
print()
print(np.mean(arr,axis = 1)) # row wise
print()
print(np.max(arr))
print()
print(np.min(arr))
print()
print(np.std(arr))
print()
print(np.var(arr))
print()
