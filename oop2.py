#inheritance
import csv
class Item:
    #class attribute
    #can be accessed by class name and object
    #can be modified by class name, overwriting is done by object but not modified
    pay_rate = 0.8

    #we assign datatype to parameters in the constructor
    #so that we can avoid any type of error

    #when an object or instance is created, the constructor(init) is called
    #automatically

    all = []
    def __init__(self,name: str,price: float,quantity=0):
        #Run validations to the received arguments
        assert price >=0, f"price {price} is not greater than or equal to 0"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to 0"

        #here name,price and quantity are the attributes of the object
        self.name = name
        self.price = price
        self.quantity = quantity

        #adding the object to the list
        Item.all.append(self)
    
    """here self(or anything) is used because python in built
       pass the object as parameter so we need to
       put self to refer to the object"""
    
    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    #use csv file to create objects
    #use class method (A class method is a method that is bound to a class rather than its object.)
    #do not use normal method because here objective is to create objects from csv
    #if normal method is written in order to call that we need to create a separate object
    @classmethod
    # class method can change the class state
    # example here we are creating objects from csv
    # example here we are adding objects to the list
    # cls is used to refer to the class
    def instantiate_from_csv(cls):
        with open("csvFile.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
            #print(item)
    @staticmethod
    # it cannot change the class state
    # unlike other methods it does not have self or cls as parameter
    def is_integer(num):
        #we will count out the floats that are point zero
        #for example 5.0, 10.0
        #if the number is float and the decimal part is zero
        #then it is an integer
        if isinstance(num,float):
            # is_integer counts out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        return False
    #method to represent the object in string
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"


class phone(Item):
    def __init__(self,name: str,price: float,quantity=0, broken=0):
        # calling the parent class constructor
        super().__init__(name,price,quantity)
        
        #Run validations to the received arguments
        
        assert broken >=0, f"broken {broken} is not greater than or equal to 0"

        self.broken = broken
        

p1=phone("Iphone",1000,10,1)
print(p1.calculate_total_price())
