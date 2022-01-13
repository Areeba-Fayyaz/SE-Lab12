import numpy as np

def compare_length(array1, array2):
    if len(array1)==len(array2):
        print("lengths are same")
    else:
        print("lengths are different")
#input !st array
arr1=np.array([])
n=int(input("enter no of elements:"))
for i in range (n):
    v=input("list item: ")
    arr1=np.append(arr1,v)

print(arr1)
#input second array
arr2=np.array([])
n=int(input("enter no of elements:"))
for i in range (n):
    v=input("list item: ")
    arr2=np.append(arr2,v)

print(arr2)

compare_length(arr1,arr2)
