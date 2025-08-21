from prouduct import products
from inventory import invent
import csv
import os

class customer(products):
    
    def calculate_price(self):
        price = 0
        for i in range(len(self.lid)):
            price += self.products[self.lid[i]][2] * self.lcount[i]
        return price
    
    def save_data(self):
        name = input("Enter your name: ")
        Age = int(input("Enter your age: "))
        contact = input("Enter your phone number: ") 
        
        price = self.calculate_price()
        print(f"Total price: {price}")
        
        data = {"Name": name, "Age": Age, "Phone Num": contact, "Total Price": price}
        
        
        file_exists = os.path.isfile("Customers_Data.csv")
        
        
        with open("Customers_Data.csv", "a", newline='', encoding='utf-8') as f:
            fieldnames = ["Name", "Age", "Phone Num", "Total Price"]
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            if not file_exists:
                dict_writer.writeheader()
            
            dict_writer.writerow(data)
        
        print("Your data has been saved successfully!")
        self.lid = []  
        self.lcount = [] 