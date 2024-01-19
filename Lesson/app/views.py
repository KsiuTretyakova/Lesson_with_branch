from django.shortcuts import render
import Students.dmytro_mohylnyi.main as func


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

n1 = input("Your number: ")
n2 = input("First number")
n3 = input("Second number")
print(func.square(n1))
print(func.min(n2, n3))