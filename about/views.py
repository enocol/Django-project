from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    about = About.objects.first()
    template_name = "about/about.html"
    return render(request, template_name, {"about": about})
