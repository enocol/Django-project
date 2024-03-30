from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.shortcuts import redirect
from django.contrib import messages 


# Create your views here.

def about(request):
    about = About.objects.first()
    form = CollaborateForm()
    template_name = "about/about.html"
    context = {"about": about,
               "form": form}
    
    
    if request.method == "POST":
        form = CollaborateForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.success(request, 'Your request has been submitted successfully')
            return redirect('about')

    return render(request, template_name, context)


