import json
import os
import config

products = []

class Product():
    def __init__(self, id:str, name:str, type:str, cost:int):
        self.id = id
        self.name = name
        self.type = type
        self.cost = cost

    def __str__(self):
        return f'Product information:\nID: {self.id}\nName: {self.name}\nType: {self.type}\nCost: {self.cost}{config.currencySymbol}'
    def __repr__(self):
        return f"Product({self.id!r})"

def chooseId(list):
    if int(list[-1].id) == (len(list)):
        return f"{(len(list)+1):05}"
    else:
        for char in list:
            if (list.index(char) - 1) >= 0 and list.index(char) < len(list):
                if (int(char.id)+1) != int(list[int(char.id)].id): # id = 00001 index = 0
                    return f"{(int(char.id)+1):05}"

def readJson(fileName):
    with open(fileName, mode='r', encoding=config.encoding) as f:
        return list(json.loads(f.read()))

def addToProducts(data:dict, list:list):
        data = dictToProduct(data)
        if int(data.id) == len(list):
            list.append(dictToProduct(data))
        else:
            list.insert((int(data.id)-1),data)

def dictToProduct(data):
    return Product(data['id'],data['name'],data['type'],data['cost'])

def loadProducts(fileName=config.defoultJsonName):
    if os.path.isfile(fileName):
        try:
            dataList = readJson(fileName)
        except:
            dataList = list

        if dataList:
            for data in dataList:
                addToProducts(data, products)
            return [True,'Products loaded successfully.']
        else:
            return [False,'Products could not be loaded.']
    else:
        return [False,'Products could not be loaded.']

def saveProducts(products, fileName=config.defoultJsonName):
    try:
        with open(fileName, 'w', encoding=config.encoding) as f:
            f.write(json.dumps([i.__dict__ for i in products]))
        return [True,'Products saved seccessfully.']
    except:
        return [False,'Products could not be saved.']
    
def createProduct():
    data = {
        'id': chooseId(products),
        'name': input('Enter product name: '),
        'type': input('Enter product type: '),
        'cost': input('Enter product cost: ')
    }
    print(dictToProduct(data))
    check = input('Would you like the information you entered to be added to the products list? (Y/n):')
    if check.upper() == "Y":
        addToProducts(data, products)
        return [True,"Products added successfully."]
    elif check.upper() == "N":
        return [False,"Adding operation cancelled."]
    else:
        createProduct()

def deleteProduct():
    try:
        Pid = int(input("Enter the product id: "))
    except:
        return [False, "No product found"]
    willBeDeleted = None
    for product in products:
        if int(product.id) == Pid:
            willBeDeleted = product
            break
    if willBeDeleted:
        print(willBeDeleted)
        check = input("Are you sure you want to permanently delete this product from your products list?\n(Y/n): ").upper()
        if check == "Y":
            del products[products.index(willBeDeleted)]
            return [True,"Product deleted successfully."]
        elif check == "N":
            return []
        else:
            print("incorrect or unknown character")
            deleteProduct()
    else:
        return [False, "No product found"]

def viewProducts():
    if products:
        for product in products:
            print("-"*10)
            print(product)
            
    else:
        print("You do not have any products.")


if __name__=="__main__":
    quit = True
    print("Shopping cart application was launched successfully.")
    while quit:
        print(f"{"-"*10}\n1. Load Products\n2. Save Products\n3. Create New Product\n4. Delete Product\n5. View Products{"\n"*2}{'"'+config.exitkey+'"'} to exit the application")
        print()
        choice = input("(1/2/3/4/5): ").upper()
        print()
        if choice == config.exitkey.upper():
            while True:
                check = input("Are you sure you want to exit the application? (Y/n): ").upper()
                if check == "Y":
                    print("Exiting the application...")
                    quit = False
                    break
                elif check == "N":
                    break
                else:
                    print("incorrect or unknown character")
                    continue

        elif choice == "1":
            print(loadProducts()[1])
        elif choice == "2":
            print(saveProducts(products)[1])
        elif choice == "3":
            print(createProduct()[1])
        elif choice == "4":
            print(deleteProduct()[1])
        elif choice == "5":
            viewProducts()
        else:
            print("Incorrect or unknown character.")