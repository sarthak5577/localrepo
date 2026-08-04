count=int(input("Enter how many Customer id's you want to insert:- "))
a=[]
for i in range(count):
    temp=int(input(f"Enter the ID's of Customer {i+1}:- "))
    a.append(temp)
number= sorted(a)

start=0
end=len(number)-1
found=False
target=int(input("Enter the ID you want to search:- "))

while start<=end:
    mid=(start+end)//2
    if number[mid]==target:
        print("Customer IDfound at index:- ",mid)
        found=True
        break
    elif number[mid]<target:
        start=mid+1
    else:
        end=mid-1
if found==False:
    print("Customer ID not found")

