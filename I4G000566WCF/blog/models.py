from django.db import models

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Author=models.CharField(max_length=20)
    Text=models.TextField(max_length=200)
    Created_date=models.DateTimeField()
    Published_date = models.DateTimeField()
    def __str__(self):
        return self.Title,self.Author,self.Text,self.Created_date,self.Published_date
    def get_user_model(self):
        return self.Author
