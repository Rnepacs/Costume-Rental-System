import datetime
import dic_read
import operations
import return_bill

#function to return costumes
returned = []
def return_():
    dic= dic_read.read1() #call function and store return value
    try:
        print("\n")
        choice = int(input("Enter the Costume ID you want to return: "))
        print("\n")
    except:
        print("\n")
        print("----------------------------------")
        print("Enter valid Cosutume ID !!")
        print("----------------------------------")
        print("\n")
        return_()

    if choice <= 0 or choice > 10:
        print("######################################## \n")
        print("\t INVALID CUSTOMER ID! \t \n")
        print("######################################## \n")
        return_()
    else:            
        costume_name = dic[choice]
        name = costume_name[0]
        print("\n")
        print("---------------------------------------------------------------------- \n")
        print("The Costume you want to return is "+name+"\n")
        print("---------------------------------------------------------------------- \n")
        return_qty =int(input("Enter the quantity of item you want to return: "))
        print("\n")
        print("\n")
        days = int(input("Enter the number of days it was rented for: "))
        print("\n")

        #add fined price to a list
        fined_price = [] #empty list for prices of empty to store
        costume_price = dic[choice] 
        price = costume_price[2]
        price = float(price.replace("$",""))
        price_f = float(price*return_qty)
        fined_price.append(price_f)
        total_fined_amount = sum(fined_price)

        #add returned item to the list
        costume_returned = dic[choice]
        costume_r = costume_returned[0]
        returned.append(costume_r)
    
        
        #update quantity in dictionary and stock.txt
        selected_item = dic[choice] 
        updated_qty= int(selected_item[3])+return_qty
        selected_item[3] = str(updated_qty)
        operations.update_stock(dic)
        validate(choice,total_fined_amount,days)

    
#function to ask if additional costume is to be returned
    
def validate(c,t,d):
    choice = c
    total_fined_amount = t
    days = d
    again = input("Do you want to return another costume? (y/n):")
    again_ = again.lower()
    if (again_ == "y"):
        return_()
    elif (again_ == "n"):
        operations.fine_calculation(total_fined_amount,days)
        return_bill.fine_bill(total_fined_amount,days,returned)
    else:
        print("---------------------------------------------------------------------- \n")
        print("Invalid input: type 'Y' or 'y' for Yes  and 'N' or 'n' for No \n")
        print("---------------------------------------------------------------------- \n")
        validate(c,t,d)
    

