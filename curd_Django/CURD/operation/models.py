from django.db import models

# Create your models here.
#
class record(models.Model):

    male = 'M'
    female = 'F'
    sex_choice = [
        (male,'male'),
        (female,'female'),
    ]
    create_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=15,
        choices=sex_choice,
        default="None")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100,default="None")
    city = models.CharField(max_length=100,default="None")
    province = models.CharField(max_length=100,default="None")
    country = models.CharField(max_length=100,default="None")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
