from django.contrib import admin

from .models import Course

# Register your models here.
# admin.site.register(Course)

@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated', 'instructor', 'published']