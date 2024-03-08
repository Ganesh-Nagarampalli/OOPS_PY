from item import Item
class phone(Item):
    def __init__(self,name: str,price: float,quantity=0, broken=0):
        # calling the parent class constructor
        super().__init__(name,price,quantity)
        
        #Run validations to the received arguments
        
        assert broken >=0, f"broken {broken} is not greater than or equal to 0"

        self.broken = broken