from django import forms

from .models import Stock, Performance, Shikiho, Note

WATCH_CHOICES = [
    ('0', 'ー'),
    ('1', 'WATCHING'),
    ('2', 'CONSIDERING'),
]
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
TYPE_CHOICES = [
    ('0', 'メモ'),
    ('1', '売買記録'),
    ('2', '分析記録'),
]

class StockForm(forms.ModelForm):
    watch_flag = forms.fields.ChoiceField(
        choices=WATCH_CHOICES,
        widget=forms.widgets.Select,
    )
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
        fields = ('stock_code', 'source','pub_year','pub_month','target_period','is_established','sales_amount', 'operating_income', 'ordinary_income', 'net_income', 'per', 'notes', 'updated_date')

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
        fields = ('stock_code', 'pub_year','pub_month','market_capitalization','capital_ratio','roe','roa', 'operating_cf', 'investing_cf', 'financing_cf', 'headline_1', 'headline_2', 'notes', 'updated_date')

class NoteForm(forms.ModelForm):
    type = forms.fields.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.widgets.Select,
    )
    class Meta:
        model = Note
        fields = ('id', 'stock_code', 'publish_date', 'type', 'summary', 'notes', 'stock_price', 'latest_high_price', 'latest_low_price', 'high_limit', 'low_limit', 'buy_price', 'profit_price', 'loss_cut_price', 'rr_rate', 'updated_date')
