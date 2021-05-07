from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views = {}
    views['reviews'] = Review.objects.all()
    views['facts'] = Fact.objects.all()
    return render(request,'index.html', views)

def about(request):
    views = {}
    views['reviews'] = Review.objects.all()
    views['qualifications'] = Qualification.objects.all()

    return render(request,'about.html', views)

def blog_home(request):
    return render(request,'blog-home.html')

def blog_single(request):
    return render(request,'blog-single.html')

def contact(request):
    views = {}
    views['inform'] = Info.objects.all()

    if request.method == "POST":
        my_name = request.POST['name']
        my_email = request.POST['email']
        my_subject = request.POST['subject']
        my_message = request.POST['message']
        data = Contact.objects.create(
            name = my_name,
            email = my_email,
            subject = my_subject,
            message = my_message
        )
        data.save()
        views['message'] = "The message is sent. Thank You "

        return render(request, 'contact.html',views )
    return render(request,'contact.html', views)

def elements(request):
    return render(request,'elements.html')

def price(request):
    views = {}
    views['myplan'] = Myplan.objects.all()

    return render(request,'price.html', views)

def services(request):
    views = {}
    views['facts'] = Fact.objects.all()
    return render(request,'services.html', views)

def portfolio(request):
    return render(request,'portfolio.html')
