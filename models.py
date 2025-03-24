from django.db import models

# Create your models here.

class Customer(models.Model):
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State/Province = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Postal_Code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.LastName + ", " + self.FirstName

class Car(models.Model):
    Serial_Number = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Year = models.IntegerField(max_length=4)
    Car_For_Sale = models.BooleanField()
    
    def __str__(self):
        return self.Make + " " + self.Model
    
class Salesperson(models.Model):
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Last_Name + ", " + self.First_Name

class Sales_Invoice(models.Model):
    Invoice_Number = models.CharField(max_length=50)
    Date = models.DateField()
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Salesperson_ID = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Invoice_Number + " " + self.Date
    
class Service_Ticket(models.Model):
    Service_Ticket_Number = models.CharField(max_length=50)
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Date_Recieved = models.DateField()
    Comments = models.CharField(max_length=150)
    Date_Returned_To_Customer = models.DateField()
    
class Mechanic(models.Model):
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Last_Name + ", " + self.First_Name
    
class Service_Mechanic(models.Model):
    Service_Ticket_ID = models.ForeignKey(Service_Ticket, on_delete=models.CASCADE)
    Service_ID = models.ForeignKey(Service, on_delete=models.CASCADE)
    Mechanic_ID = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    Hours = models.IntegerField()
    Comment = models.CharField(max_length=150)
    Rate = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.Service_Ticket_ID + " " + self.Service_ID
    
    
class Parts(models.Model):
    Part_Number = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Purchase_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Retail_Price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.Part_Number + " " + self.Description
    
class Parts_Used(models.Model):
    Part_ID = models.ForeignKey(Parts, on_delete=models.CASCADE)
    Service_Ticket_ID = models.ForeignKey(Service_Ticket, on_delete=models.CASCADE)
    Number_Used = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    
class Service(models.Model):
    Service_Name = models.CharField(max_length=50)
    Hourly_Rate = models.DecimalField(max_digits=10, decimal_places=2)
    