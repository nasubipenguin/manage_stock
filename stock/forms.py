from django import forms

from .models import Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('stock_code','stock_name','accounting_month','business_type','ir_url','watch_flag','notes',)