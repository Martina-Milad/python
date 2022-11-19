import os
import time

while True:


    time.sleep(0.1)
    os.system('cls')

    for i in range(0,18,1):
        print("            ",end="")
        if(i<6)|(i>11):
            for j in range(0,6,1):
                if (j==5):
                    print("*",end="")
                else:
                    print(" ",end="")
            print(" ")
        else:
            for z in range(i-6,5,1):
                    print(" ",end="")
            for j in range(0,(2*(i-6)+1),1):  
                    print("*",end="")
            print(" ")

    time.sleep(0.1)
    os.system('cls')

    for i in range(0,6,1):
        print("\n")

    c=1
    for i in range(0,11,1):
        for x in range(0,18,1):
            print(" ",end="")
        for k in range(0,6,1):
            if (i!=5):
                print(" ",end="")
            if(i==5):
                print("**",end="")
        for j in range(0,c,1):
            print('*',end='')
        if (i<5):
            c=c+1
        if (i>=5):
            c=c-1
        print("")

    time.sleep(0.1)
    os.system('cls')

    for i in range(0,9,1):
        print("\n")
    for i in range(0,18,1):
        print("            ",end="")
        if(i<6)|(i>11):
            for j in range(0,6,1):
                if (j==5):
                    print("*",end="")
                else:
                    print(" ",end="")
            print(" ")
        else:
            for z in range(0,i-6,1):
                    print(" ",end="")
            for z in range(0,11-(2*(i-6)),1):  
                    print("*",end="")
            print(" ")

    time.sleep(0.1)
    os.system('cls')

    for i in range(0,6,1):
        print("\n")
    c=1
    for i in range(0,11,1):
        for k in range(0,6,1):
            if (i!=5):
                print(" ",end="")
            if(i==5):
                print("**",end="")
        for m in range(0,6-c,1):
            print(" ",end="")
        for j in range(0,c,1):
            print('*',end='')
        if (i<5):
            c=c+1
        if (i>=5):
            c=c-1
        print("")
