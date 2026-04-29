from django.shortcuts import render
from django.contrib import messages
from Home.models import Contact
import datetime

# Create your views here.
def home(request):
    return render(request, "index.html")

def learn(request):
    return render(request, "learn.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        description = request.POST.get("description")
        contact = Contact(name=name, email=email, phone=phone, description=description, date = datetime.date.today())
        contact.save()

        messages.success(request, "Your message has been sent successfully!")
    return render(request, "contact.html")

def calculator(request):
    return render(request, "calculator.html")
#calcualtors inside this--
def sip_calculator(request):
    return render(request, "sip_calculator.html")
def mf_calculator(request):
    return render(request, "mf_calculator.html")
def ppf_calculator(request):
    return render(request, "ppf_calculator.html")
def swp_calculator(request):
    return render(request, "swp_calculator.html")

def scams(request):
    return render(request, "scams.html")

def search(request):
    query = request.GET.get("q", "")  # Get search keyword

    # Here you can search your models (example)
    # results = Article.objects.filter(title__icontains=query)

    return render(request, "search_results.html", {
        "query": query,
        # "results": results,
    })