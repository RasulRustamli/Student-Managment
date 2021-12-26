import os
import platform

global listStd 
listStd = ["yugesh", "kishor", "gajen", "Gopi"]  


def manageStudent(): 

    x = "#" * 30
    y = "=" * 28
    global bye  
    bye = "\n {}\n# {} #\n# ===> Brought To You By <===  #\n# ===>  <===  #\n# {} #\n {}".format(
        x, y, y, x)

    # Printing Welcome Message And options For This Program
    print(""" 
  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------
Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		
		""")
 

    try: 
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")  # Error Message
    else:
        print("\n")  # Print New Line

    # Checking Using Opti
        print("List Students\n")
        for students in listStd:
            print("=> {}".format(students))

    elif(userInput == 2):  
        newStd = input("Enter New Student: ")
        if(newStd in listStd):  
            print("\nThis Student {} Already In The Database".format(
                newStd))  # Error Message
        else:
            listStd.append(newStd)
            print("\n=> New Student {} Successfully Add \n".format(newStd))
            for students in listStd:
                print("=> {}".format(students))
 

    elif(userInput == 3): 
        srcStd = input("Enter Student Name To Search: ")
        if(srcStd in listStd): 
            print("\n=> Record Found Of Student {}".format(srcStd))
        else:
            print("\n=> No Record Found Of Student {}".format(
                srcStd))  # Error Message

    elif(userInput == 4):  
        rmStd = input("Enter Student Name To Remove: ")
        if(rmStd in listStd):  
            listStd.remove(rmStd)
            print("\n=> Student {} Successfully Deleted \n".format(rmStd))
            for students in listStd:
                print("=> {}".format(students))
        else:
            # Error Message
            print("\n=> No Record Found of This Student {}".format(rmStd))

    elif(userInput < 1 or userInput > 4):  
        print("Please Enter Valid Option")  # Error Message



manageStudent()


def runAgain():  
    runAgn = input("\nwant To Run Again Y/n: ")
    if(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"): 
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageStudent()
        runAgain()
    else:
        quit(bye)  


runAgain()