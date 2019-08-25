from django.contrib import admin
from .models import Editor, Category, Image, Location

# Register your models here.


# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal = ('editor',)
    
admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
