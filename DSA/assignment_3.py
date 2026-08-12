#bubble sorting
def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

no=int(input("Enter the number of elements in the array: "))
print("Enter unsorted array elements:-")
arr=[]
for i in range(no):
    ele=int(input(f"Enter the element {i+1}:- ")) 
    arr.append(ele)

sort(arr)
print("Array after sorting:", arr)

#selection sorting 
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        si=i
        for j in range(i+1,n):
            if arr[j]<arr[si]:
                si=j
        arr[i],arr[si]=arr[si],arr[i]
        
n=int(input("Enter the number of elements in the array: "))
print("--Enter unsorted array elements--")
arr=[]
for i in range(n):
    ele=int(input(f"Enter the element {i+1}:- ")) 
    arr.append(ele)

selection_sort(arr)
print("Array after selection sorting:", arr)