import datetime

def bill(r,t,b,q,cp): #function to print the bill

    dt=datetime.datetime.now()
    y = str(dt.year)
    m = str(dt.month)
    d = str(dt.day)
    h = str(dt.hour)
    minu = str(dt.minute)
    sec = str(dt.second)
    cdt = d+"/"+m+"/"+y+"   "+h+":"+minu+":"+sec
    rented=r
    total_price =t
    brand_list = b
    qty_list = q
    price_list = cp
    customer_name = input("Enter your name: ")

   #bill written in .txt file
    file = open(customer_name+".txt","w")
    file.write("-------------------------------------------------------------------------------------------- \n")
    file.write("                                       INVOICE                                               \n")
    file.write("-------------------------------------------------------------------------------------------- \n")
    file.write("Name : "+customer_name+"\n")
    file.write("Date   : "+d+"/"+m+"/"+y+"\n")
    file.write("Time   : "+h+":"+minu+":"+sec+"\n")

    id_length = len(rented)+1 #lenght of rented list which stores rented items
    for i in range(1,id_length):
            rented_print = rented[i-1] #assigin variable to rented index value : get costume name
            brand_list_print = brand_list[i-1] #assign variable to rented index value : get brand name
            qty_list_print = qty_list[i-1] #assign variable to rented index value : get quantity rented
            price_list_print = price_list[i-1] #assign variable to rented index value : get price 
            file.write("("+str(i)+")"+" "+str(rented_print)+" : "+str(brand_list_print)+"  "+"Qty("+str(qty_list_print)+")"+" "+str(price_list_print)+"\n")
    file.write("-------------------------------------------------------------------------------------------- \n")    
    file.write("Grand total: $"+str(total_price)+"\n")
    file.write("--------------------------------------------------------------------------------------------\n")

    file.close()
        
    #bill print in the program    
    print("\n")
    print("-----------------------------------------------------------------------------------------")
    print("                                     BILL DETAILS                                                        ")
    print("-----------------------------------------------------------------------------------------")
    print("Name of the customer: ", customer_name)
    print("Date and time of borrow: ", cdt)
    print("Total price is: ","$",total_price ) 
    print("The items are: ", rented) 
    print("The brand of items are: ",brand_list)
    print("-----------------------------------------------------------------------------------------")
    print("\n")
       
