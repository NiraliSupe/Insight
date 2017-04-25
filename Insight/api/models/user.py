from django.db import models


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

class User(models.Model):
    first_name    = models.CharField(max_length=32, null=False)
    last_name     = models.CharField(max_length=32, null=False)
    gender        = models.CharField(choices=GENDER_CHOICES, max_length=6)
    age           = models.IntegerField(null=False)
    
    class Meta:
       #managed  = True
       db_table = 'user'

    def __str__(self):
        return self.id
