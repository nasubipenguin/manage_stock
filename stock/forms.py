from django import forms

from .models import Stock, Performance, Shikiho

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('stock_code','stock_name','accounting_month','business_type','ir_url','watch_flag','notes', 'updated_date')

class PerformanceForm(forms.ModelForm):

    class Meta:
        model = Performance
        fields = ('source','pub_year','pub_month','target_period','is_established','sales_amount', 'operating_income', 'ordinary_income', 'net_income', 'per', 'updated_date')

class ShikihoForm(forms.ModelForm):

    class Meta:
        model = Shikiho
        fields = ('pub_year','pub_month','market_capitalization','capital_ratio','roe','roa', 'operating_cf', 'investing_cf', 'financing_cf', 'headline_1', 'headline_2', 'notes', 'updated_date')
