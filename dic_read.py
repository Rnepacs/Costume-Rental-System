def read1():
        costume_dic={}
        file = open("stock.txt","r") #open stock.txt file in read mode
        costume_data = file.read()  #read the file and assign it to costume_data
        costume_data = costume_data.split("\n")

        #this while loop is used to remove empty string in a list
        while("" in costume_data):
                costume_data.remove("")
                
        count = 0
        #loop to split data in tabular format
        for i in range(len(costume_data)):
            count=count+1
            costume_dic[count]=(costume_data[i].split(","))
        return costume_dic


        
