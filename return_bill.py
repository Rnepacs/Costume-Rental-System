import datetime
import operations

def fine_bill(t,day_,r): #function to print the bill
    total_fined_amount = t
    days = day_
    returned =str(r)
    dt=datetime.datetime.now()
    y = str(dt.year)
    m = str(dt.month)
    d = str(dt.day)
    h = str(dt.hour)
    minu = str(dt.minute)
    sec = str(dt.second)
    cdt = d+"/"+m+"/"+y+"   "+h+":"+minu+":"+sec

   #fine_bill written in .txt file
    print("\n")
    n = input("Enter your name: ")
    print("\n")
    fine_ = float(operations.fine_calculation(total_fined_amount,days))
    file = open("fine for "+n+".txt","w")
    file.write("-------------------------------------------------------------------------------------------- \n")
    file.write("                                       BILL FOR FINED AMOUNT                                          \n")
    file.write("-------------------------------------------------------------------------------------------- \n")
    file.write("Name : "+n+"\n")
    file.write("Date   : "+d+"/"+m+"/"+y+"\n")
    file.write("Time   : "+h+":"+minu+":"+sec+"\n")
    file.write("List of returned item: "+returned)
    file.write("-------------------------------------------------------------------------------------------- \n")
    file.write("The customer is fined for $"+str(fine_))
    file.write("-------------------------------------------------------------------------------------------- \n")

    file.close()
        
    #bill print in the program    
    print("\n")
    print("-----------------------------------------------------------------------------------------")
    print("                                     FINED AMOUNT                                                     ")
    print("-----------------------------------------------------------------------------------------")
    print("Name of the customer: ", n)
    print("Date and time of return: ", cdt)
    print("List of returned item: ", returned)
    print("Fined Amount: ",fine_)
    print("-----------------------------------------------------------------------------------------")
    print("\n")

