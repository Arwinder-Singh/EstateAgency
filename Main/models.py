from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.\
class Amenities(models.Model):
    amenities_name=models.CharField(max_length=50)   
    def __str__(self):
        return self.amenities_name
    
class Agent(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='profile_pics')
    description=models.TextField()
    phone=models.CharField(max_length=12)
    mobile=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)
    skype = models.URLField(max_length=200)
    fb = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    insta = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

class Property(models.Model):
    prop_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    price=models.FloatField(max_length=50)
    description=models.TextField()
    propertyType=models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField(null=True,default=0)
    map_location=models.URLField()
    floor_plans=models.ImageField(upload_to='floor_plans')
    amenities=models.ManyToManyField(Amenities)
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE,related_name='agentProperty')
    
    
    def __str__(self):
        return self.prop_name
    
class Image(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name="propertyImages")
    building=models.ImageField(upload_to='property')
    def __str__(self):
        return self.property.prop_name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='posts')
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date=models.DateField()
    content=RichTextField(blank=True,null=True)
    
    def __str__(self):
        return "posted by " + self.author + '-' + self.title
    
class postComments(models.Model):
    naam = models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    comment=models.TextField()
    timestamp=models.DateTimeField(default=datetime.now())
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="postComment")
    def __str__(self):
        return  self.comment

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message=models.TextField()
    
    def __str__(self):
        return  "message from " + self.name+ " (subject- " +self.subject+" )"
    
    
    

    
    
    
    
    
    
    
    
    
