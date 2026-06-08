from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def destination(request):
    return render(request, 'destination.html')

def hotel(request):
    return render(request, 'hotel.html')

def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')