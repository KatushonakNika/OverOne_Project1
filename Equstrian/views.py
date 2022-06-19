from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main(request):
    return render(request, 'main/main_page.html')


def about(request):
    return render(request, 'main/about_page.html')

