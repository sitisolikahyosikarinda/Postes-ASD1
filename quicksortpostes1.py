import os 
import random

def quickSort(arr):
    # jika panjang array <=1 maka kembalikan array 
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
#  nilai yang lebih kecil dati pivot 
        left = [x for x in arr[1:] if x <= pivot]   
# nilai yang lebih besar dari pivot 
        right = [x for x in arr [1:] if x >= pivot] 
# kembalikan semua nilai beserta pivot nya 
        return quickSort(left) + [pivot] + quickSort(right)

kosong =[]  
ar =  range(1,100)
arr = random.sample(ar,k=10)          
kosong = arr


print(f"List Sebelum partitioning {arr}")

result = quickSort(arr)

print(f"List setelah partitioning {result}")