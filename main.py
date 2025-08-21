from inventory import invent
from prouduct import products
from customer import customer

cust = customer()

while True:
    print("Select your operation:\n" 
          "1: Show products\n"
          "2: Buy products\n"
          "3: Check stock\n"
          "4: Calculate price\n"
          "5: Exit")

    operation = int(input("Enter choice: "))

    if operation == 1:
        cust.show_items()
    elif operation == 2:
        cust.show_items()
        cust.buy()
        cust.save_data()
    elif operation == 3:
        item_id = int(input("Enter item id: "))
        cust.check_stock(item_id)
    elif operation == 4:
        price = cust.calculate_price()
        print(f"Total price: {price}")                   
    else:
        break