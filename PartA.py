class Pet:
    def __init__(self, name, age, sex, petID, owner_name):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.owner_name = owner_name
    
    def displayInfo(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Sex: " + self.sex)
        print("Pet ID: " + str(self.petID))
        print("Owner's Name: " + self.owner_name)
        
    def updateName(self, name):
        self.name = name
        
    def updateAge(self, age):
        self.age = age
        
    def updateSex(self, sex):
        self.sex = sex
    
    def updatePetID(self, petID):
        self.petID = petID
        
    def updateOwnerName(self, owner_name):
        self.owner_name = owner_name
        
    
class Dog(Pet):
    def __init__(self, name,age, sex, petID, owner_name, breed):
        super().__init__(name, age,sex, petID, owner_name)
        self.breed = breed
    
    def displayInfo(self):
        super().displayInfo()
        print("Breed: " + self.breed)
        
    def updateBreed(self, breed):
        self.breed = breed
        

class Cat(Pet):
    def __init__(self, name, age, sex, petID, owner_name, declawed):
        super().__init__(name, age, sex, petID, owner_name)
        self.declawed = declawed
    
    def displayInfo(self):
        super().displayInfo()
        print("Declawed?: " + str(self.declawed))
        
    def updateDeclawed(self, declawed: bool):
        if not isinstance(declawed, bool):
            raise ValueError("Declawed must be a boolean")
        self.declawed = declawed
        
class Bird(Pet):
    def __init__(self, name, age, sex, petID, owner_name, wings_clipped):
        super().__init__(name, age, sex, petID, owner_name)
        self.wings_clipped = wings_clipped
        
    def displayInfo(self):
        super().displayInfo()
        print("Wings Clipped?: " + str(self.wings_clipped))
        
    def updateWingsClipped(self, wings_clipped: bool):
        if not isinstance(wings_clipped, bool):
            raise ValueError("Wings Clipped must be a boolean")
        self.wings_clipped = wings_clipped
   
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
print("Before Updates:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
d1 = Dog("Fido", 5, "M", 1, "John Doe", "Golden Retriever")
d1.displayInfo()
d1.updateName("Rex")
d1.updateAge(6)
d1.updateSex("F")
d1.updatePetID(2)
d1.updateOwnerName("Little Timmy")
d1.updateBreed("Labrador Retriever")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("After Updates:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
d1.displayInfo()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
print("Before Updates:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
c1 = Cat("Whiskers", 3, "F", 4, "Jane", True)
c1.displayInfo()
c1.updateName("Mittens")
c1.updateAge(4)
c1.updateSex("M")
c1.updatePetID(5)
c1.updateOwnerName("Jacob Bobvinzky")
c1.updateDeclawed(False)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("After Updates:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
c1.displayInfo()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
print("Before Updates:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
b1 = Bird("Tweety", 1, "F", 7, "Jackie Chan", True)
b1.displayInfo()
b1.updateName("Polly")
b1.updateAge(2)
b1.updateSex("M")
b1.updatePetID(8)
b1.updateOwnerName("Jill Mackenzie")
b1.updateWingsClipped(False)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("After Updates:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
b1.displayInfo()