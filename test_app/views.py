from django.shortcuts import render , redirect
from urllib import request
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

def religousart(request):
    return render(request,'religousart.html')

def hover(request):
    return render(request,'hover.html')

def glitterpainting(request):
    return render(request,'glitterpainting.html')

def religouspainting(request):
    return render(request,'religouspainting.html')

def pouringtechnique(request):
    return render(request,'pouringtechnique.html')

def landscape(request):
    return render(request,'landscape.html')

def flowers(request):
    return render(request,'flowers.html')

def woodpainting(request):
    return render(request,'woodpainting.html')

def otherproducts(request):
    return render(request,'otherproducts.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
