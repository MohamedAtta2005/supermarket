class invent :
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

    def check_stock (self,items_id) :

        for i in items_id :
            if self.products[i][3] == 0 :
                return True

    def check_low_stock (self,items_id) :

        for i in items_id :
            if self.products[i][3] <= 3 :
                return True

