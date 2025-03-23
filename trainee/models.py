from django.db import models
from course.models import Course  # Import the Course model from the course app

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)  # Trainee's name
    age = models.IntegerField(default=5)  # Trainee's age with a default value of 5
    email = models.EmailField(unique=True)  # Unique email address
    picture = models.ImageField(upload_to='trainee_pictures/', blank=True, null=True)  # Optional profile picture
    courses = models.ManyToManyField(Course, related_name='trainees')  # Many-to-many relationship with Course
