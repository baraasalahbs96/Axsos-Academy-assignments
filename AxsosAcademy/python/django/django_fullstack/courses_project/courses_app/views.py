from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

def validate_course(data):
    errors = {}
    name = data.get('name', '').strip()
    description = data.get('description', '').strip()

    if not name:
        errors['name'] = 'Name is required'
    elif len(name) <= 5:
        errors['name'] = 'Name must be more than 5 characters'

    if not description:
        errors['description'] = 'Description is required'
    elif len(description) <= 15:
        errors['description'] = 'Description must be more than 15 characters'

    return errors

def index(request):
    all_courses = Course.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'courses': all_courses})

def create(request):
    if request.method != 'POST':
        return redirect('index')

    errors = validate_course(request.POST)
    if errors:
        all_courses = Course.objects.all().order_by('-created_at')
        return render(request, 'index.html', {
            'errors': errors,
            'data': request.POST,
            'courses': all_courses
        })

    Course.objects.create(
        name=request.POST['name'].strip(),
        description=request.POST['description'].strip()
    )
    return redirect('index')

def destroy_confirm(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'destroy.html', {'course': course})

def destroy(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        course.delete()
    return redirect('index')