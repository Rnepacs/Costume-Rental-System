import datetime
import dic_read
import rent_operation

 #create an empty dictionary


def rent():  #function to rent
        dic = dic_read.read1()
        #costume_dic={}
        print("------------------------------------------------------------------------------------------")
        print(" ID \t  Name \t                 Brand \t                  Price        Quantity")
        print("------------------------------------------------------------------------------------------")
        display(dic)
        
def display(d): #function to display data in tables properly
    dic = d
    count = 0
    #loop to print costume items, brand, price, and quantity in tabular format
    for key,value in dic.items(): 
        count = count + 1    
        print(key, end ='\t')
        for i in value:
            print(i, end='\t')
        print("\n")   
    rent_operation.validate_quantity(count)






