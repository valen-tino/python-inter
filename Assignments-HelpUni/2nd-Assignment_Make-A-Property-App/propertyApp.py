class property:
    def __init__ (self, location="", price=0, propertyType="", size=0):
        self.location = location
        self.price = price
        self.propertyType = propertyType
        self.size = size

    def getLocation(self):
        return self.location

    def getPrice(self):
        return self.price

    def getPropertyType(self):
        return self.propertyType

    def getSize(self):
        return self.size

    def setLocation(self, location):
        self.location = location

    def setPrice(self, price): 
        self.price = price

    def setPropertyType(self, propertyType):
        self.propertyType = propertyType
    
    def setSize(self, size):
        self.size = size

    def typeString(self):
        if self.propertyType == 'A' or self.propertyType == 'a':
            return "apartment"
        elif self.propertyType == 'B' or self.propertyType == 'b':
            return "bungalow"
        elif self.propertyType == "C" or self.propertyType == 'c':
            return "condominium"

    def annualTax(self):
        if self.propertyType == 'A' or self.propertyType == 'a':
            return self.price * 0.025
        elif self.propertyType == 'B' or self.propertyType == 'b':
            return self.price * 0.045
        elif self.propertyType == "C" or self.propertyType == 'c':
            return self.price * 0.035
        return 0
    
    def __eq__(self, obj):
        if self.obj.location == self.location and self.obj.propertyType == self.propertyType and self.obj.size == self.size:
            return True
        else:
            return False

    def __lt__(self, obj):
        if self.obj.size < self.size:
            return True
        else:
            return False

    def __le__(self, obj):
        if self.obj.size <= self.size:
            return True
        else:
            return False

    def __str__(self):
        return self.typeString().capitalize() + ", " + str(self.size) + " square feet, at " + self.location.capitalize() + ", costing $" + str(self.price)


class propertyList:
    def __init__(self, groupName=""):
        self.groupName = groupName
        self.propertyCollection = []
    
    def getGroupName(self): 
        return self.groupName

    def getPropertyCollection(self):
        return propertyCollection

    def setGetGroupName(self):
        self.groupName = groupName 
    
    def addProperty(self, obj):
        self.propertyCollection.append(obj)

    def noOfProperties(self):
        result = str(len(self.propertyCollection))
        
        return result

    def allProperties(self):
        display = ""
        for i in range(len(self.propertyCollection)):
            display = display + str(self.propertyCollection[i]) + "\n"

        return display

    def totalPrice(self):
        totalFee = 0
        for i in range(len(self.propertyCollection)):
            totalFee = totalFee + self.propertyCollection[i].getPrice()

        return totalFee

    def mostExpensiveProperty(self):
        self.priceCollection = [] #a new list to store the price
        for i in range(len(self.propertyCollection)):
            #a code to add the price in the list to the new list that store the price
            self.priceCollection.append(self.propertyCollection[i].getPrice())
        
        maxValue = max(self.priceCollection)
        index = self.priceCollection.index(maxValue)
        result = str(self.propertyCollection[index])
        
        return result
        
    def findPropertyByType(self, aptType):
        self.typeCollection = []
        for i in range(len(self.propertyCollection)):
            #a code to add the price in the list to the new list that store the price
            self.typeCollection.append(self.propertyCollection[i].getPropertyType())
        
        index = self.typeCollection.index(aptType)
        result = str(self.propertyCollection[index])
        
        return result

def main():
    p1 = property("Batubulan", 200, "a", 55)
    p2 = property("Batuan", 50, "b", 275)
    p3 = property("Gianyar", 1000, "c", 28)  
    print("Annual Tax: " + str(p1.annualTax()) + "\n")
    
    l1 = propertyList("Valen")
    l1.addProperty(p1)
    l1.addProperty(p2)
    l1.addProperty(p3)
    
    print("Example Property Type with Details: "  + "\n")
    print("Total Properties: " + l1.noOfProperties() + "\n")
    print("List of all properties:\n" + l1.allProperties() + "\n")
    print("Total Price: " + "$" +str(l1.totalPrice()) + "\n")
    print("Most Expensive Property:\n" + l1.mostExpensiveProperty())
main()  
