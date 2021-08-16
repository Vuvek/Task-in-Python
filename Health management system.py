import datetime as d
print("-------------------------------------------------------",end = '\n')
print("-------------------------------------------------------",end = '\n')
print("             HEALTH MANAGEMENT SYSTEM                ")
print("-------------------------------------------------------",end = '\n')
print("-----------------------------------------------------1--",end = '\n')
print("  What would you like to lock diet or retrieve diet  ")
print("  Press 1 for Locking diet  \n  Press 2 for retrieving diet  ")
s = int(input())
if(s == 1):
    print("  Enter Name To Whom Diet would You Like To Lock: ")
else:
    print("  Enter Name To Whom Diet would You Like To Retrieve: ")
print("   1  Rohan \n   2  Harry \n   3  Mohan ")

Name = input()

def Date():
    x = d.datetime.now()
    return x

def Set():
    if(Name == 'Rohan'):
        print("Please lock the diet of Rohan")
        with open('Rohan.txt','w+') as f:
            r = input()
            f.write(r)
        print("Diet of Rohan is locked in file ")
    elif(Name == 'Mohan'):
        print("Please lock the diet of Mohan")
        with open('Mohan.txt','w+') as f:
            m = input()
            f.write(m)
        print("Diet of Rohan is locked in file ")
    elif(Name == 'Harry'):
        print("Please lock the diet of Harry")
        with open('Harry.txt','w+') as f:
            h = input()
            f.write(h)
        print("Diet of Rohan is locked in file ")
def Get():
    if (Name == 'Rohan'):
        with open('Rohan.txt', 'r+') as f:
            print([Date()],":",f.read())
    elif (Name == 'Mohan'):
        with open('Mohan.txt', 'r+') as f:
            print([Date()],":",f.read())
    elif (Name == 'Harry'):
        with open('Harry.txt', 'r+') as f:
            print([Date()],":",f.read())

if(s == 1):
    Set()

else:
    Get()




