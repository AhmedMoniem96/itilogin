from django.contrib import admin
from django.urls import path, include
from .views import home  # Import home view
from django.conf.urls.static import static
from django.conf import settings  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='trainee/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', home, name='home'),  
    path('admin/', admin.site.urls),
    path('trainees/', include('trainee.urls')),
    path('courses/', include('course.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    