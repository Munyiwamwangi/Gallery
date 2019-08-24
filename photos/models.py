from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    travel = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    epic = models.CharField(max_length=50)
    landscape = models.CharField(max_length=50)
    portrait = models.CharField(max_length=50)
    heritage = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='articles/', default="")
    image_name = models.CharField(max_length=50)
    descritption = models.TextField()
    url = models.CharField(max_length=2000)
    location = models.ForeignKey(Editor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
        
    def update_image(self):
            self.save()
        
    def delete_image(self):
        self.delete()

    @classmethod
    def search_image_category(cls, search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
    
    @classmethod
    def get_image_by_id(cls, image_id):
        photos = cls.objects.filter(title__icontains=image_id)
        return photos
    
    @classmethod
    def search_by_location(cls, search_term):
        photos = cls.objects.filter(location__icontains=search_term)
        return photos
