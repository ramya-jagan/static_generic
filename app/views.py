from django.shortcuts import render

# Create your views here.
def html1(request):
  return render(request,'html1.html')

def coff(request):
  return render(request,'coff.html')

def register(request) :
  return render(request,'register.html') 