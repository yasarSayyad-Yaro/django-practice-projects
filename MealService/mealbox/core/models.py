from django.db import models

# Create your models here.
class Customer(models.Model):
    subscription_CHOICES=[
        ('lunch','Lunch'),('dinner','Dinnner'),('both','Both')
    ]
    name=models.CharField(max_length=100)
    subscription_type=models.CharField(max_length=10,choices=subscription_CHOICES)
    phone=models.CharField(max_length=12)
    address=models.TextField()
    total_meals=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Mealdelivery(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.DateField()
    lunch_delivered=models.BooleanField(default=False)
    dinner_delivered=models.BooleanField(default=False)

    class Meta:
        unique_together=('customer','date')
