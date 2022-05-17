from django.shortcuts import render


def mainpage(request):
    return render(request,'main/mainpage.html')

def europe(request):
    return render(request,'main/europe.html')

def asia(request):
    return render(request,'main/asia.html')

def russia(request):
    return render(request,'main/russia.html')

def america(request):
    return render(request,'main/america.html')
# Create your views here.

