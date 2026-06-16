import numpy as np 

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.mean(arr))
print(np.var(arr,axis = 0))
print(np.mean(arr,axis = 1))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print(np.var(arr))