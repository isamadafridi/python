class Pet:
    def  __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    

class Dog(Pet):
    # def __init__(self, breed):
    #     self.__breed = breed

    # def set_breed(self, breed):
    #     self.__breed = breed

    # def get_breed(self):
    #     return self.__breed
    def __init__(self, name, animal_type, age, breed):
        Pet.__init__(self, name, animal_type, age)
        self.__breed = breed