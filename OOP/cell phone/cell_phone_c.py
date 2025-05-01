class CellPhone:
    def __init__(slef, manufact, model, price):
        slef.__manufact = manufact
        slef.__model = model
        slef.__retail_price = price
    
    #the set_model method accepts an argument. The argument is assigned to the __model attribute
    def set_manufact(self, manufact):
        self.__manufact = manufact
    
    def set_model(self, model):
        self.__model = model
    
    def set_retail_price(self, price):
        self.__retail_price = price
    
    #the get method returns the value of the __model attribute
    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self): 
        return self.__retail_price
    
