from django.views.generic import ListView
from .models import Student
from django.utils.translation import gettext as _

class StudentListView(ListView):
    model = Student
    template_name = "students.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('学生列表')
        return context
"""
def all_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
"""
