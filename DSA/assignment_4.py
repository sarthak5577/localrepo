MAX = 5

queue = [None] * MAX
front = -1
rear = -1


# Add a call to the queue
def addCall(customerID, callTime):
    global front, rear

    # Check if queue is full
    if rear == MAX - 1:
        print("Queue is full. Cannot add call.")
        return

    # If first call is being added
    if front == -1:
        front = 0

    # Increase rear
    rear = rear + 1

    # Store customer ID and call time
    queue[rear] = (customerID, callTime)

    print("Call added successfully.")


# Answer and remove the first call
def answerCall():
    global front, rear

    # Check if queue is empty
    if front == -1:
        print("No calls waiting.")
        return

    customerID, callTime = queue[front]

    print("Answering call...")
    print("Customer ID:", customerID)
    print("Call Time:", callTime, "minutes")

    # If this was the last call
    if front == rear:
        front = -1
        rear = -1
    else:
        front = front + 1


# View all calls in the queue
def viewQueue():

    if front == -1:
        print("Queue is empty.")
        return

    print("\nCalls currently waiting:")

    for i in range(front, rear + 1):
        customerID, callTime = queue[i]

        print("Customer ID:", customerID, " and Call Time:", callTime, "minutes")


# Check whether queue is empty
def isQueueEmpty():

    if front == -1:
        return True
    else:
        return False


# Main program
while True:

    print("\n===== CALL CENTER QUEUE =====")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Queue Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        customerID = int(input("Enter Customer ID: "))
        callTime = int(input("Enter Call Time (minutes): "))

        addCall(customerID, callTime)

    elif choice == 2:

        answerCall()

    elif choice == 3:

        viewQueue()

    elif choice == 4:

        if isQueueEmpty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == 5:

        print("Program terminated.")
        break

    else:

        print("Invalid choice!")
