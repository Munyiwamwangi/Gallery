from django.db import models
import datetime as dt

# Create your models here.

class Category(models.Model):
    image_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Location(models.Model):
    image_location = models.CharField(max_length =50)

    def __str__(self):
        return self.name
    
class Editor(models.Model):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=100, default='Anonymous')
    phone_number = models.CharField(max_length=10, blank=True)
    

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/', default="")
    title = models.CharField(max_length=50)
    descritption = models.TextField()
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        Location, 
        on_delete=models.CASCADE)
    editor = models.ManyToManyField(Editor)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
        
    def update_image(self):
            self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def todays_images(cls):
        today = dt.date.today()
        images = cls.objects.filter(pub_date__date=today)
        return images

    @classmethod
    def search_image_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
    
    @classmethod
    def get_image_by_id(cls, image_id):
        images = cls.objects.filter(title__icontains=image_id)
        return images
    
    @classmethod
    def search_by_location(cls, search_term):
        images = cls.objects.filter(location__icontains=search_term)
        return images
