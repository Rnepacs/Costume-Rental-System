import rent
import operations
import option
import return_



print("")
print("########################################################")
print("\t WELCOME TO COSTUME RENTAL PROGRAM")
print("########################################################")
print("\n")

loop = True
while loop == True: #lwhile loop to run till its true
    option.option()
    print("")
    
    try:
        n = int(input("Enter your option:"))
    except:
        print("\n")
        print("----------------------------------")
        print("Enter valid input value!")
        print("----------------------------------")
        print("\n")
        option.option()
   
    #condition check for input to call needed function
    if n ==1:
        rent.rent()
    elif n ==2:
        return_.return_()
    elif n ==3:
        print("\n \n")
        print("\t \t \t Thank you for using our application. \t \t \t \n")
        exit()
    else:
        print("\n")
        print("Choose from given service options!!!")
        print("\n")
    
        
        
        
        
        






    
    
        
