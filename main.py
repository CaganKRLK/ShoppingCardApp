import json
import os
import config


products = []

class product():
    def __init__(self, id:str, name:str, type:str, cost:int):
        self.id = id
        self.name = name
        self.type = type
        self.cost = cost

    def __str__(self):
        return f'Product Infos\nID: {self.id}\nName: {self.name}\nType: {self.type}\nCost: {self.cost}'
    def __repr__(self):
        return f"Product({self.id!r})"

def addProducts(data):
        products.append(product(data['id'],data['name'],data['type'],data['cost']))

def loadProducts(fileName=config.defoultJsonName):
    if os.path.isfile(fileName):
        with open(fileName, mode='r', encoding=config.encoding) as f:
            dataList = list(json.loads(f.read()))

        if dataList:
            for data in dataList:
                addProducts(data)
            return 'Products loaded successfully'
    else:
        return 'Products could not be loaded'


def saveProducts(products, fileName=config.defoultJsonName):
    try:
        with open(fileName, 'w', encoding=config.encoding) as f:
            f.write(json.dumps([i.__dict__ for i in products]))
        return 'Products saved seccessfully'
    except:
        return 'Products could not be saved'
    
def createProducts():
    dataList = {
        'id': f"{(len(products)+1):05}",
        'name': input('Ürün adını girin: '),
        'type': input('Ürün tipini girin: '),
        'cost': input('Ürün fiyatını girin: ')
    }

    addProducts(dataList)