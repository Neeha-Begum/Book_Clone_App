from django.db import models

# Create your models here.
class Book(models.Model):
    author=models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="media",null=True,blank=True)
    file=models.FileField(upload_to="media",null=True)
    title=models.CharField(max_length=100,null=True)
    genre=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)

    def __str__(self):
        return self.genre
    
class Author(models.Model):
    name=models.CharField(max_length=50,null=True)
    published_year=models.IntegerField(null=True)
    nationality=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name