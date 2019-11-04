from django.conf import settings
from django.db import models
from django.utils import timezone


# Stock
class Stock(models.Model):
    stock_code = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=50)
    accounting_month = models.IntegerField()
    business_type = models.CharField(max_length=20)
    ir_url = models.URLField(blank=True, null=True)
    watch_flag = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.stock_code + ':' + self.title


# Performance
class Performance(models.Model):
    stock_code = models.ForeignKey(Stock, to_field='stock_code', on_delete=models.CASCADE)
    source = models.IntegerField()
    pub_year = models.IntegerField()
    pub_month = models.IntegerField()
    target_period = models.IntegerField()
    is_established = models.IntegerField()
    sales_amount = models.IntegerField()
    operating_income = models.IntegerField()
    ordinary_income = models.IntegerField()
    net_income = models.IntegerField()
    per = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


# Shikiho
class Shikiho(models.Model):
    stock_code = models.ForeignKey(Stock, to_field='stock_code', on_delete=models.CASCADE)
    pub_year = models.IntegerField()
    pub_month = models.IntegerField()
    market_capitalization = models.IntegerField()
    capital_ratio = models.FloatField()
    roe = models.FloatField()
    roa = models.FloatField()
    operating_cf = models.BooleanField()
    investing_cf = models.BooleanField()
    financing_cf = models.BooleanField()
    headline_1 = models.CharField(max_length=200)
    headline_2 = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

