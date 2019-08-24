from django.contrib import admin
from .models import Editor, Category, Image, Locate

# Register your models here.
    
admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Locate)
