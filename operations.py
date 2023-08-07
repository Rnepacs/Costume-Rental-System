import dic_read


#fucntion to update_stock in .txt file
def update_stock(c):
    costume_dic=c
    f = open("stock.txt", "w")
    for value in costume_dic.values():
        f.write(",".join(value))
        f.write("\n")
    f.close

   
def fine_calculation(t,d):
    total_fined_amount = t
    days = d
    if days > 7:
        fine = float((days-7)*(0.1*total_fined_amount)) #calculation for fine of 1 percent of item price per day above 7 day of rental
        print("")
        print("You are fined "+str(fine))
        print("\n")
    else:
        print("----------------------------------------------------------------------------------------- \n")
        print("Thank you! Costume returned before due date. \n")
        print("----------------------------------------------------------------------------------------- \n")
    return fine 

    

