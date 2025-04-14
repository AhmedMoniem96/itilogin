from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm  
from django.contrib.auth.decorators import login_required

# ✅ Ensure user is logged in before accessing courses
@login_required
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})  # ✅ matches new path
0
# ✅ Create a new course
@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # ✅ Match correct URL name
    else:
        form = CourseForm()
    return render(request, 'course/create.html', {'form': form})

# ✅ Update an existing course
@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # ✅ Match correct URL name
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/form.html', {'form': form})

# ✅ Delete a course
@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')  # ✅ Match correct URL name
    return render(request, 'courses/course_confirm_delete.html', {'course': course})
