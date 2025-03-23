from django.urls import path
from .views import trainee_list, trainee_add, trainee_update, trainee_delete  
from .views import CustomLoginView, CustomLogoutView, courses_list , register
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('add/', trainee_add, name='trainee_add'),
    path('update/<int:pk>/', trainee_update, name='trainee_update'),
    path('delete/<int:pk>/', trainee_delete, name='trainee_delete'),  
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='trainee/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('courses/', courses_list, name='courses'),

]
