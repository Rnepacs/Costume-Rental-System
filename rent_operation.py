import dic_read
import operations
import option
import bill

rented = [] #empty list to store rented item for bill
total_price =[]
brand_list=[]
qty_list = []
price_list =[]

def validate_quantity(c): #function to compare and check the quantity and entered quantity
    count = c
    try:
        choice = int(input("Enter the costume ID: "))
    except:
        print("\n")
        print("----------------------------------")
        print("Enter valid Cosutume ID !!")
        print("----------------------------------")
        print("\n")
        validate_quantity(c)
        
    print("")
    print("The Costume ID is ",choice)
    print("")

    
    
    if choice > 0 and choice <= c: #loop to check customer entered quantity amount
        print("############################## \n")
        print("\t Ready to rent \t \n")
        print("############################## \n")
        print("")
        qty = int(input("Enter the quantity: "))
        dic = dic_read.read1()
        selected_item = dic[choice]
        #loop to check and compare quantity of costume present in stock
        if int(selected_item[3]) ==0: #checks if custome is in stock or not
            print("\n")
            print("-------------------------------------------")
            print("The costume is out of stock!")
            print("-------------------------------------------")
            print("\n")
            validate_quantity(c)
                    
        elif int(selected_item[3])<qty and selected_item[3]!=0 : 
            print("\n")
            print("-------------------------------------------")
            print("Your entry exceeds the item available")
            print("-------------------------------------------")
            print("\n")
            validate_quantity(c)
        else:
            print("\n")
            print("-------------------------------------------")
            print("Costume is available!")
            print("-------------------------------------------")
            print("\n")
            #update item stock
            updated_qty= int(selected_item[3])-qty
            selected_item[3] = str(updated_qty)
            operations.update_stock(dic)
            
            
            #add selected items to list to present in bill
            costume_chosen = dic[choice]
            costume_c = costume_chosen[0]
            rented.append(costume_c)

            #add brand of selected items to list to present in bill
            brand_chosen=dic[choice]
            brand_c=brand_chosen[1]
            brand_list.append(brand_c)

            #add quantity to the list to present in bill
            qty_list.append(qty)
            

            #add total price to present in bill
            costume_price = dic[choice] 
            costume_p = costume_price[2]
            price_list.append(costume_p)
            costume_p = costume_p.replace("$","") #replacing dollar sign with nothing
            bill_price = float(costume_p)*qty #total price = item price * quantity
            total_price.append(bill_price) 
            total_bill_price = sum(total_price) #sum of prices in the list 
            multiple_purchase(rented,total_bill_price,brand_list,count,qty_list,price_list)       
    else:
        print("######################################## \n")
        print("\t INVALID CUSTOMER ID! \t \n")
        print("######################################## \n")
        validate_quantity(c)

def multiple_purchase(r,t,b,c,q,cp): #function to allow multiple purchase
    count = c
    rented = r
    total_price = t
    brand_list = b
    qty_list = q
    price_list = cp
    print("")
    z = input("Does the customer want to rent another item? (y/n): ")
    another_item = z.lower()
    print("")
    if ( another_item  == "y"):
        validate_quantity(count)
    elif another_item  =="n":
        print("\n")
        print("##############################")
        print("READY TO GENERATE YOUR BILL!")
        print("##############################")
        print("\n")
        bill.bill(rented,total_price,brand_list,qty_list,price_list)
    else:
        print("Invalid input: type 'Y' or 'y' for Yes  and 'N' or 'n' for No")
        print("")
        multiple_purchase(r,t,b,c,q,cp)
