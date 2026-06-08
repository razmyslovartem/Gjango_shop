  # catalog/views.py
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name} ваш номер:{phone} и сообщение:{message} отправлены!")
    return render(request, "catalog/contacts.html")