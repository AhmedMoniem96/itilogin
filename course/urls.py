from django.urls import path
from . import views
from .views import courses_list, course_create, course_update, course_delete 


urlpatterns = [
    path('', views.courses_list, name='course_list'), 
    path('create/', views.course_create, name='course_create'),
    path('update/<int:pk>/', views.course_update, name='course_update'),
    path('delete/<int:pk>/', views.course_delete, name='course_delete'),
]