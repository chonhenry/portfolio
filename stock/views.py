from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.
def home(request):
    #pk_59f2b887b82a45b298477654529b5f55
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_59f2b887b82a45b298477654529b5f55")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'stock/home.html', {'api': api})
    else:
        return render(request, 'stock/home.html', {'ticker': 'Enter a ticker symbol'})

def about(request):
    return render(request, 'stock/about.html', {})

#@login_required
def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added."))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        i = 0

        #for ticker_item in ticker:
        while i < len(ticker):
            ticker_item = ticker[i]
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_59f2b887b82a45b298477654529b5f55")
            try:
                api = json.loads(api_request.content)
                output.append([api, ticker_item])
            except Exception as e:
                api = "Error..."
            i+=1

        lst = len(ticker)
        return render(request, 'stock/add_stock.html', {'ticker': ticker, 'output': output, 'list': lst})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted."))
    return redirect('add_stock')

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'stock/delete_stock.html', {'ticker':ticker})

def signup(request):
    if request.method=='POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'stock/signup.html', {'error':'Username has been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('add_stock')
        else:
            return render(request, 'stock/signup.html', {'error2':'Password not match'})
    else:
        return render(request, 'stock/signup.html')

def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('add_stock')
        else:
            return render(request, 'stock/login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'stock/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('stock')











#
