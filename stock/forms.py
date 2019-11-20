from django import forms

from .models import Stock, Performance, Shikiho

SOURCE_CHOICES = [
    ('0', ''),
    ('1', '四季報'),
    ('2', '会社発表'),
]
PLUS_MINUS_CHOICES = [
    ('', ''),
    ('True', '+'),
    ('False', '-'),
]

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('stock_code','stock_name','accounting_month','business_type','ir_url','watch_flag','notes', 'updated_date')

class PerformanceForm(forms.ModelForm):
    source = forms.fields.ChoiceField(
        choices=SOURCE_CHOICES,
        widget=forms.widgets.Select,
    )

    class Meta:
        model = Performance
        fields = ('source','pub_year','pub_month','target_period','is_established','sales_amount', 'operating_income', 'ordinary_income', 'net_income', 'per', 'updated_date')

class ShikihoForm(forms.ModelForm):
    operating_cf = forms.fields.ChoiceField(
        choices=PLUS_MINUS_CHOICES,
        widget=forms.widgets.Select,
    )
    investing_cf = forms.fields.ChoiceField(
        choices=PLUS_MINUS_CHOICES,
        widget=forms.widgets.Select,
    )
    financing_cf = forms.fields.ChoiceField(
        choices=PLUS_MINUS_CHOICES,
        widget=forms.widgets.Select,
    )
    class Meta:
        model = Shikiho
        fields = ('pub_year','pub_month','market_capitalization','capital_ratio','roe','roa', 'operating_cf', 'investing_cf', 'financing_cf', 'headline_1', 'headline_2', 'notes', 'updated_date')
