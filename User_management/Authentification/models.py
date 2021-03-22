from django.db import models



ROLE_CHOICES = [
    ('admin', 'ADMIN'),
    ('superuser','SUPERUSER'),
    ('user', 'USER'),
]


class User(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255 , unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255 ,choices=ROLE_CHOICES , default='user')
    def __str__(self):
        return self.role
    def __str__(self):
        return self.name

    
    


   
    
