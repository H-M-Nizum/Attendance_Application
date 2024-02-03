from django.shortcuts import render

# Create your views here.

def attendance_pageviews(request, class_slug = None):
    # data = models.StudentModel.objects.all()
    if class_slug is not None:
        cl_name = models.SchoolclassModel.objects.get(slug = class_slug)
        data = models.StudentModel.objects.filter(cl_name = cl_name)
    
    classnames = models.SchoolclassModel.objects.all()
    
    return render(request, 'showstudent.html', {'classname': classnames})
def take_attendance(request):
    pass