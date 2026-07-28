 #Library Borrowing Records

n = int(input("Enter the number of library members: "))

# Create a list of size n
borrow = [0] * n

# Input borrow counts
for i in range(n):
    borrow[i] = int(input("Enter books borrowed by member " + str(i + 1) + ": "))

# 1. Calculate Average
total = 0
for i in range(n):
    total = total + borrow[i]

average = total / n
print("\nAverage books borrowed:", average)

# 2. Find Highest and Lowest Borrow Count
highest = borrow[0]
lowest = borrow[0]

for i in range(1, n):
    if borrow[i] > highest:
        highest = borrow[i]

    if borrow[i] < lowest:
        lowest = borrow[i]

print("Highest borrow count:", highest)
print("Lowest borrow count:", lowest)

# 3. Count Members with Zero Borrowings
zero_count = 0

for i in range(n):
    if borrow[i] == 0:
        zero_count = zero_count + 1

print("Members who borrowed no books:", zero_count)

# 4. Find Mode (Most Frequent Borrow Count)
mode = borrow[0]
max_count = 0

for i in range(n):
    count = 0

    for j in range(n):
        if borrow[i] == borrow[j]:
            count = count + 1

    if count > max_count:
        max_count = count
        mode = borrow[i]

print("Most frequently borrowed count (Mode):", mode)