__author__ = 'lyndsay.beaver'
stockList = ["ALR", "BTS", "CRK"]
priceList = [10, 20, 30]

numStocks = len(stockList)

def listStocks():
    for i in range(numStocks):
        print("The stock is {} and it's price is {}".format(stockList[i], priceList[i]))
        changePrices(priceList)

def changePrices(priceList):
    for i in range(numStocks):
        priceList[i] += 3
        print(priceList())




print(listStocks())
#changePrices()

