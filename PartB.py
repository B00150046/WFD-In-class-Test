import unittest
from PartA import *

d2 = Dog("Fido", 5, 'M', 1, "John", "Golden Retriever")
c2 = Cat("Whiskers", 8, 'F', 2, "Jane", True)
b2 = Bird("Buttercup", 21, 'F', 3, "Jack", True)

def instance_Of_Class(Object , Class):
    return isinstance(Object, Class)
        
def not_instance_Of_Class(Object , Class):
    return not isinstance(Object, Class)

def is_Identical(Object1 , Object2):
    return Object1 == Object2
        
class UnitTestQ2(unittest.TestCase):
    def test_isInstance(self):
        self.assertTrue(instance_Of_Class("Fido", str))
        self.assertTrue(instance_Of_Class(5, int))
        self.assertTrue(instance_Of_Class("M", str))
    
    def test_isNotInstance(self):
        self.assertTrue(not_instance_Of_Class("Fido", int))
        self.assertTrue(not_instance_Of_Class(5, str))
        self.assertFalse(not_instance_Of_Class("M", str))
    
    def test_isIdentical(self):
        ob1 = [1,2,3]
        ob2 =['a','b','c']
        ob3 = ob2
        self.assertTrue(is_Identical(ob1, ob1))
        self.assertTrue(is_Identical(ob2, ob3))
        self.assertFalse(is_Identical(ob1, ob2))
        
    def test_updateName(self):
        d2.updateName("Rex")
        c2.updateName("Mittens")
        b2.updateName("Polly")
        self.assertEqual(d2.name, "Rex")
        self.assertEqual(c2.name, "Mittens")
        self.assertEqual(b2.name, "Polly")
        
    def test_updateAge(self):
        d2.updateAge(6)
        c2.updateAge(4)
        b2.updateAge(2)
        self.assertEqual(d2.age, 6)
        self.assertEqual(c2.age, 4)
        self.assertEqual(b2.age, 2)
        
    def test_updateSex(self):
        d2.updateSex("F")
        c2.updateSex("M")
        b2.updateSex("M")
        self.assertEqual(d2.sex, "F")
        self.assertEqual(c2.sex, "M")
        self.assertEqual(b2.sex, "M")
    
    def test_updatePetID(self):
        d2.updatePetID(2)
        c2.updatePetID(5)
        b2.updatePetID(8)
        self.assertEqual(d2.petID, 2)
        self.assertEqual(c2.petID, 5)
        self.assertEqual(b2.petID, 8)
        
    def test_updateOwnerName(self):
        d2.updateOwnerName("Jane")
        c2.updateOwnerName("Jack")
        b2.updateOwnerName("Jack")
        self.assertEqual(d2.owner_name, "Jane")
        self.assertEqual(c2.owner_name, "Jack")
        self.assertEqual(b2.owner_name, "Jack")
        
    def test_isDeclawed(self):
        c2.updateDeclawed(False)
        self.assertEqual(c2.declawed, False)
    
    def test_wingsClipped(self):
          b2.updateWingsClipped(False)
          self.assertEqual(b2.wings_clipped, False)
         
    def test_updateBreed(self):
        d2.updateBreed("Labrador Retriever")
        self.assertEqual(d2.breed, "Labrador Retriever")
        
        
if __name__ == '__main__':
    unittest.main()