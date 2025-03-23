from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    videos = models.IntegerField(default=0)  
    image = models.ImageField(upload_to='course_pictures/', blank=True, null=True)  
    videos = models.FileField(upload_to='course_videos/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name