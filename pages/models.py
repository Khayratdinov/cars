from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 150)
    photo = models.ImageField(upload_to="media/photo/Teams/")
    facebook_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    telegram_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.first_name
    

    
    
    
    