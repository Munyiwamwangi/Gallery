from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=50)


    def save_category(self):
        self.save()
        
    @classmethod
    def delete_location(cls, location):
        cls.objects.filter(location=location).delete()

    def __str__(self):
        return self.location
class Category(models.Model):
    category = models.CharField(max_length=50, default='Epic')

    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls, category):
        cls.objects.filter(category=category).delete()
    
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
    url = models.TextField(default="")
    pub_date = models.DateTimeField(auto_now_add=True)
    editor = models.ManyToManyField(Editor)

    location = models.ForeignKey(
        Location, 
        on_delete=models.DO_NOTHING)
    category = models.ForeignKey(
        Category, 
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

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
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        # images = cls.objects.filter(categories__icontains=search_term)
        images = cls.objects.filter(category__category=search_term) 
        return images
    
    @classmethod
    def get_image_by_id(cls,number):
        return cls.objects.get(pk = number)

    @classmethod
    def search_by_location(cls, search_term):
        images = cls.objects.filter(location__icontains=search_term)
        return images

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images
