queue=[]
front= None

#Function to add elements into the queue
def Enqueue(que):
    item=eval(input("Enter meber number number,name and age"))
    que.append(item)
    if len(que)==1:
        front=rear=0
    else:
        rear=len(que)-1
    
#Function to delete/remove elements from the queue
def Dequeue(que):
    if que==[]:
        print("Underflow! Queue is empty")
        return 
    else:
        item=que.pop(0)
    if len(que)==0:
        front=rear=None
    else:
        rear=len(que) - 1
    print("Deleted Item = ", item)
        

#Function to display elements in the Queue
def display(que):
    if que==[]:
        print("Queue is empty")
    elif len(que)==1:
        print(que[0],"<--front, rear")
    else:
        front=0
        rear=len(que)-1
        print(que[front],"<--front")
        for i in range (1,rear):
             print(que[i])
        print(que[rear],"<--Rear")


#Main program - Menu
while True:
    print("Queue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    ch=int(input("Enter your Choice"))
    if ch==1:
        Enqueue(queue)
    elif ch==2:
        Dequeue(queue)
    elif ch==3:
        display(queue)
    elif ch==4:
        break
    else:
        print("Invalid Choice")
