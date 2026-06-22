from django.shortcuts import redirect, render

from .models import Contact, NewUser

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
    if request.method == 'POST':
        if NewUser.objects.filter(
            email=request.POST.get('email'),
            password=request.POST.get('password')).exists():
            return render(request, 'index.html')
        else:
            return redirect('/login/')
    else: 
        return render(request, 'login.html')
    

def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        users = NewUser(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        users.save()
        return redirect('/login/')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')