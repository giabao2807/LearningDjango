from django.contrib import admin
from django import forms
from .models import Category, Lesson, Course, Tag
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        field = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "created_date", "course", "active"]
    search_fields = ["subject", "created_date", "course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]

    def avatar(self, lesson):
        return mark_safe(("<img src='/static/{img_url}' alt='{alt}' width='120px'/>").format(img_url=lesson.image.name, alt=lesson.subject))


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ["avatar"]

    def avatar(self, course):
        return mark_safe(('<img src="/static/{img_url}" alt="{alt}" width="120px" />').format(img_url=course.image.name, alt=course.subject))

# Register your models here.
admin.site.register(Category)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)


