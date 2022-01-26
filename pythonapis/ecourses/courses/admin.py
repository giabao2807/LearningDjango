from django.contrib import admin
from .models import Category,Lesson,Course,Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Course)