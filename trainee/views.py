from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('courses')  # Redirect to courses after registering
    else:
        form = UserCreationForm()
    return render(request, 'trainee/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'trainee/login.html'  # Create this template
    redirect_authenticated_user = True

@login_required
def courses_list(request):
    return render(request, 'courses/course_list.html')  # Create this template

class CustomLogoutView(LogoutView):
    next_page = 'login'

    
def trainee_list(request):
    trainees = Trainee.objects.prefetch_related('courses').all()  # Prefetch courses
    return render(request, 'trainee/list.html', {'trainees': trainees})


def trainee_create(request):
    if request.method == "POST":
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')  # Redirect after saving
    else:
        form = TraineeForm()

    return render(request, 'trainee/add.html', {'form': form})




def trainee_add(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add.html', {'form': form})





def trainee_update(request, pk):
    trainee = get_object_or_404(Trainee, id=pk)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/update.html', {'form': form})



def trainee_delete(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    trainee.delete()
    return redirect('trainee_list')
