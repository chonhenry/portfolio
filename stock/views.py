from django.shortcuts import render

# Create your views here.
def home(request):
    #pk_59f2b887b82a45b298477654529b5f55
    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_59f2b887b82a45b298477654529b5f55")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'stock/home.html', {'api': api})

def about(request):
    return render(request, 'stock/about.html', {})
