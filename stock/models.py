from django.conf import settings
from django.db import models
from django.utils import timezone


# Stock
class Stock(models.Model):
    stock_code = models.IntegerField(primary_key=True, unique=True)
    stock_name = models.CharField(max_length=50)
    accounting_month = models.IntegerField()
    business_type = models.CharField(max_length=20)
    ir_url = models.URLField(blank=True, null=True)
    watch_flag = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stock_code) + ':' + self.stock_name

# Performance
class Performance(models.Model):
    class Meta:
        unique_together = ('stock_code', 'source', 'pub_year', 'pub_month', 'target_period')

    stock_code = models.ForeignKey(Stock, on_delete=models.CASCADE)
    source = models.IntegerField()
    pub_year = models.IntegerField()
    pub_month = models.IntegerField()
    target_period = models.IntegerField()
    is_established = models.BooleanField()
    sales_amount = models.IntegerField()
    operating_income = models.IntegerField()
    ordinary_income = models.IntegerField()
    net_income = models.IntegerField()
    sales_amount_yoy = models.IntegerField(default=0, null=True)
    operating_income_yoy = models.IntegerField(default=0, null=True)
    ordinary_income_yoy = models.IntegerField(default=0, null=True)
    net_income_yoy = models.IntegerField(default=0, null=True)
    per = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stock_code) + '[' + str(self.source)  + ' ' + str(self.pub_year)  + '/' + str(self.pub_month) + ']'+ ':' + str(self.target_period)


# Shikiho
class Shikiho(models.Model):
    class Meta:
        unique_together = ('stock_code', 'pub_year', 'pub_month')

    stock_code = models.ForeignKey(Stock, on_delete=models.CASCADE)
    pub_year = models.IntegerField()
    pub_month = models.IntegerField()
    market_capitalization = models.FloatField()
    capital_ratio = models.FloatField()
    roe = models.FloatField()
    roa = models.FloatField()
    operating_cf = models.IntegerField()
    investing_cf = models.IntegerField()
    financing_cf = models.IntegerField()
    headline_1 = models.CharField(blank=True, null=True, max_length=200)
    headline_2 = models.CharField(blank=True, null=True, max_length=200)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stock_code) + '[' + str(self.pub_year)  + '/' + str(self.pub_month) + ']'


# Note
class Note(models.Model):
    stock_code = models.ForeignKey(Stock, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    type = models.IntegerField(default=0)
    summary = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    stock_price = models.IntegerField(blank=True, null=True)
    latest_high_price = models.IntegerField(blank=True, null=True)
    latest_low_price = models.IntegerField(blank=True, null=True)
    buy_price = models.IntegerField(blank=True, null=True)
    profit_price = models.IntegerField(blank=True, null=True)
    loss_cut_price = models.IntegerField(blank=True, null=True)
    buy_amount = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stock_code) + '[' + str(self.created_date) + ']'
