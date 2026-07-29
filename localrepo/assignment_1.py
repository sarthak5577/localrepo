memcount=int(input("Enter the number of members in library:- "))
borrowed=[]
for i in range(memcount):
    name=int(input(f"Enter the book borrowed by member {i+1}:- "))
    borrowed.append(name)
total=0
for j in range(len(borrowed)):
    total=total+borrowed[j]
print("Total book borrowed:- ", total)
avg= total/memcount
print("Average book borrowed by each member:- ", avg)
for k in range(memcount):
    if borrowed[k]==max(borrowed):
        print(f"Member {k+1} borrowed maximum book that is :- ", borrowed[k])
    if borrowed[k]==min(borrowed):
        print(f"Member {k+1} borrowed minimum book that is :- ", borrowed[k])
    if borrowed[k]==0:
        print(f"Member {k+1} borrowed no book that is :- ", borrowed[k])
#for frequncy of borrowed 
max_count=0
max_borrowed=""
for i in borrowed:
    count=0
    for j in borrowed:
        if i==j:
            count+=1
    if count>max_count:
        max_count=count
        max_borrowed=i
if max_count==0:
    print("No book borrowed frequently")
else:
    print("Most frequently borrowed  is:- ",max_borrowed)