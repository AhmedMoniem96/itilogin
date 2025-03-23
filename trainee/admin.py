from django.contrib import admin
from .models import Trainee

@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')
    filter_horizontal = ('courses',)  