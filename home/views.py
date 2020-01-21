from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect('http://henrychon.co/')
    #return render(request, 'home/homepage.html')
