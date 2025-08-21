from inventory import invent

class products (invent) :

 def buy(self):
    
    while True:
        id = int(input("enter product id: \n"))
        count= int(input("enter product count: \n"))
        if(id >=200 and id <=219):
            pass
        else:
            print("id is not exist!")
            continue
                    
        if(self.check_stock(id)):
            print("product is not exist")
            continue
        elif(self.check_stock_count(id , count)):
            print(f"this quantity is not available\n Availabil quantity is : {self.products[id][3]} ")
            continue
        else:
            self.lid.append(id)
            self.lcount.append(count)
            self.products[id][3] -= count
            #   print(f"product count is :{self.products[id][3]}")
        x = input("Do you want any thing more Y|N \n")
        if(x == "Y" or x == "y"):
                continue
        else:
            print(f"{self.lid} and {self.lcount} is purchased")
            break   

 def calculate_price (self) :
        price = 0
        for i in range(len(self.lid)) :
            price += self.products[self.lid[i]][2]*self.lcount[i]
        self.lcount.append(price)
        print(price)



# pro = products()
# pro.calculate_price()