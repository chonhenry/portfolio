from django import forms
from .models import Stock, UserStock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]

class UserStockForm(forms.ModelForm):
    class Meta:
        model = UserStock
        fields = ["username", "ticker"]
