from django.shortcuts import render, redirect
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

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added."))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request, 'stock/add_stock.html', {'ticker': ticker})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted."))
    return redirect('add_stock')











#
