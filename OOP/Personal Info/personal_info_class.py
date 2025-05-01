class Personal_info:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    def name(self, name):
        self.__name = name

    def address(self, address):
        self.__address = address

    def age(self, age):
        self.__age = age

    def phone(self, phone):
        self.__phone = phone
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone
    