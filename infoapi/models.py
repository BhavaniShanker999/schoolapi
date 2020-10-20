from django.db import models

# Create your models here.
class school_model(models.Model):
    Name=models.CharField(max_length=50)
    Founder=models.CharField(max_length=25)
    Location=models.TextField()
    Branches= models.PositiveIntegerField()
    Total_staff=models.PositiveIntegerField()
    def __str__(self):
        return self.Name

class staff_model(models.Model):
    GENDER_CHOICES = ( 
    ("MALE", "MALE"),("FEMALE","FEMALE"))
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    Subjects=models.CharField(max_length=25)
    Skills=models.TextField()
    Experience_in_years= models.PositiveIntegerField()
    Present_salary=models.PositiveIntegerField()
    def __str__(self):
        return self.Name
