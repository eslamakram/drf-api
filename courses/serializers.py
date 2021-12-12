from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'instructor', 'updated', 'timestamp', 'content','published']
        model = Course