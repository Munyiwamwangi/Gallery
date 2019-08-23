from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length = 60)
    editor = models.ForeignKey(
        Editor,
        on_delete=models.DO_NOTHING)
    image_name =models.CharField(max_length=50)
    image = models.ImageField(upload_to='articles/',default="")
    descritption = models.TextField()