#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# video url: https://youtu.be/VGrRdUunjXg

theList = [0,0,0,0,0]
for i in range(5):
    theList[i] = int(input("Enter number {i = 1}:"))
    for i in theList:
        print(i)
    theList.sort()
    print("Small to large:")
    for i in theList:
        print(i)
    print("Large to small:")
    theList.sort(reverse=True)
    for i in theList:
        print(i)
    total = 0
    amount = len(theList)
    for i in theList:
        total += i
        average = total / amount
        print(f"the mean is {average} and the median is {theList[2]}")
           

theList = [0,0,0,0,0]
for i in range(len(theList)):
        theList[i] = int(input(f"Enter number {i + 1}:"))
        for i in theList:
            print(i)
        theList.sort()
        print("Small to large:")
        for i in theList:
            print(i)
        print("Large to small:")
        theList.sort(reverse=True)
        for i in theList:
            print(i)
        total = 0
        amount = len(theList)
        for i in theList:
            total += i
            average = total / amount
        
print(f"the mean is {average} and the median is {theList[2]}")
           

