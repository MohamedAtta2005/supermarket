class invent:
 order = {}

 def __init__(self):
        self.products = {
            200: ["apple", "fruits", 10, 8],
            201: ["banana", "fruits", 5, 15],
            202: ["orange", "fruits", 6, 12],
            203: ["grapes", "fruits", 12, 9],
            204: ["mango", "fruits", 15, 7],
            205: ["tomato", "vegetables", 4, 20],
            206: ["potato", "vegetables", 3, 25],
            207: ["onion", "vegetables", 2, 30],
            208: ["carrot", "vegetables", 4, 18],
            209: ["cucumber", "vegetables", 5, 14],
            210: ["milk", "dairy", 12, 10],
            211: ["cheese", "dairy", 20, 6],
            212: ["yogurt", "dairy", 8, 13],
            213: ["butter", "dairy", 18, 5],
            214: ["bread", "bakery", 7, 16],
            215: ["cake", "bakery", 25, 4],
            216: ["biscuits", "bakery", 10, 11],
            217: ["chicken", "meat", 50, 7],
            218: ["beef", "meat", 70, 5],
            219: ["fish", "meat", 40, 9],
        } 
            
 def check_stock(self, items_id) :
       
            if self.products[items_id][3] == 0 :
                return True

 def check_stock_count (self,item_id, count) :
       
            if self.products[item_id][3] < count :
                return True
 def buy(self):
      lid = []
      lcount =[]
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
              print("this quantity is not available")
              continue
          else:
              lid.append(id)
              lcount.append(count)
              self.products[id][3] -= count
              print(f"product count is :{self.products[id][3]}")
              
          x = input("continue or not \n")
          if(x == "yes"):
              continue
          else:
              print(f"{lid} and {lcount} is purchased")
              break   
              
 def show_items(self):
     for i in self.products.keys():    
      print("product_id",i,":" ,"product_name :" ,self.products[i][0]) 
 def check_low_stock (self,items_id) :

       
             if self.products[items_id][3] <= 3 :
                return True
        
