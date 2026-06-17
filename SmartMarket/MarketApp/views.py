from django.shortcuts import redirect, render

from .models import Contact

# Create your views here.

def about(request):
    return render(request, 'about.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        message = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        message.save()
        return redirect('/contact/')
    else:
        return render(request, 'contact.html')

def destination(request):
    return render(request, 'destination.html')

def hotel(request):
    return render(request, 'hotel.html')

def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')