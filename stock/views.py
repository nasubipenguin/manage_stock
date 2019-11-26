import math

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import Http404
from .models import Stock, Shikiho, Performance
from .forms import StockForm, ShikihoForm, PerformanceForm


# Stock
#----------------------------------
def stock_list(request):
    stocks = Stock.objects.filter(updated_date__lte=timezone.now())
    if request.GET.get('watch_flag'):
        stocks = stocks.filter(watch_flag__exact=request.GET.get('watch_flag'))
    if request.GET.get('stock_code'):
        stocks = stocks.filter(stock_code__exact=request.GET.get('stock_code'))
    if request.GET.get('stock_name'):
        stocks = stocks.filter(stock_name__contains=request.GET.get('stock_name'))
    stocks = stocks.order_by('stock_code')
    return render(request, 'stock/stock_list.html', {'title': 'Stock List', 'stocks': stocks})

def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        stock_code = request.POST['stock_code']
        if Stock.objects.filter(stock_code=stock_code).exists():
            return render(request, 'stock/stock_edit.html', {'title': 'Register Stock Info', 'form': form, 'exists': True})
        if form.is_valid():
            stock = form.save(commit=False)
            stock.updated_date = timezone.now()
            stock.save()
            # save -> info
            return redirect('stock_info', stock_code=stock.stock_code)
        else:
            # not_valid -> new
            return render(request, 'stock/stock_edit.html', {'title': 'Register Stock Info', 'form': form, 'is_edit': False})
    else:
        form = StockForm()
    # new
    return render(request, 'stock/stock_edit.html', {'title': 'Register Stock Info', 'form': form, 'is_edit': False})

def stock_info(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    return render(request, 'stock/stock_info.html', {'title': 'Stock Info', 'stock': stock})

def stock_edit(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.updated_date = timezone.now()
            stock.save()
            # save -> info
            return redirect('stock_info', stock_code=stock.stock_code)
        else:
            # not_valid -> edit
            return render(request, 'stock/stock_edit.html', {'title': 'Register Stock Info', 'stock_code': stock_code, 'form': form, 'is_edit': True})
    else:
        form = StockForm(instance=stock)
        form.fields['stock_code'].widget.attrs['disabled'] = 'disabled'
    # edit
    return render(request, 'stock/stock_edit.html', {'title': 'Update Stock Info', 'stock_code': stock_code, 'form': form, 'is_edit': True})

def stock_delete(request, stock_code):
    try:
        stock = Stock.objects.get(stock_code=stock_code)
    except Stock.DoesNotExist:
        raise Http404
    stock.delete()
    return redirect('stock_list')

# Shikiho
#----------------------------------
def shikiho_new(request, stock_code):
    if request.method == "POST":
        form = ShikihoForm(request.POST)
        stock_code = request.POST['stock_code']
        pub_year = request.POST['pub_year']
        pub_month = request.POST['pub_month']
        if Shikiho.objects.filter(stock_code=stock_code, pub_year=pub_year, pub_month=pub_month).exists():
            # duplicate -> edit
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code':stock_code, 'pub_year':pub_year, 'pub_month':pub_month, 'form': form, 'exists': True})
        if form.is_valid():
            shikiho = form.save(commit=False)
            shikiho.updated_date = timezone.now()
            stock = Stock.objects.get(stock_code=stock_code)
            shikiho.stock_code = stock
            shikiho.save()
            # save -> info
            return redirect('shikiho_info', stock_code=stock_code, pub_year=shikiho.pub_year, pub_month=shikiho.pub_month)
        else:
            # not_valid -> new
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'pub_year':pub_year, 'pub_month':pub_month, 'form': form, 'is_edit': False})
    else:
        form = ShikihoForm()
    # new
    return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'form': form, 'is_edit': False})

def shikiho_info(request, stock_code, pub_year, pub_month):
    shikiho = get_object_or_404(Shikiho, stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    return render(request, 'stock/shikiho_info.html', {'title': 'Shikiho Info', 'stock_code': stock_code, 'shikiho': shikiho})

def shikiho_edit(request, stock_code, pub_year, pub_month):
    shikiho = get_object_or_404(Shikiho, stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    if request.method == "POST":
        form = ShikihoForm(request.POST, instance=shikiho)
        if form.is_valid():
            shikiho = form.save(commit=False)
            shikiho.updated_date = timezone.now()
            stock = Stock.objects.get(stock_code=stock_code)
            shikiho.stock_code = stock
            shikiho.save()
            # save -> info
            return redirect('shikiho_info', stock_code=stock_code, pub_year=shikiho.pub_year, pub_month=shikiho.pub_month)
        else:
            # not_valid -> edit
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'pub_year': pub_year, 'pub_month': pub_month, 'form': form, 'is_edit': True})
    else:
        form = ShikihoForm(instance=shikiho)
        form.fields['pub_year'].widget.attrs['disabled'] = 'disabled'
        form.fields['pub_month'].widget.attrs['disabled'] = 'disabled'
    # edit
    return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'pub_year': pub_year, 'pub_month': pub_month, 'form': form, 'is_edit': True})

def shikiho_delete(request, stock_code, pub_year, pub_month):
    try:
        shikiho = Shikiho.objects.get(stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    except Shikiho.DoesNotExist:
        raise Http404
    shikiho.delete()
    return redirect('stock_detail', stock_code=stock_code)

# Performance
#----------------------------------
def performance_new(request, stock_code):
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        stock_code = request.POST['stock_code']
        source = request.POST['source']
        pub_year = request.POST['pub_year']
        pub_month = request.POST['pub_month']
        target_period = request.POST['target_period']
        if Performance.objects.filter(stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period).exists():
            # duplicate -> edit
            return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock_code':stock_code, 'source':source, 'pub_year':pub_year, 'pub_month':pub_month, 'target_period':target_period, 'form': form, 'exists': True})
        if form.is_valid():
            performance = form.save(commit=False)
            performance.updated_date = timezone.now()
            stock = Stock.objects.get(stock_code=stock_code)
            performance.stock_code = stock
            performance.save()
            # save -> info
            return redirect('performance_info', stock_code=stock_code, source=performance.source, pub_year=performance.pub_year, pub_month=performance.pub_month, target_period=target_period)
        else:
            # not_valid -> new
            return render(request, 'stock/performance_edit.html', {'title': str(form.errors)+'Register Performance Info', 'stock_code': stock_code, 'source':source, 'pub_year':pub_year, 'pub_month':pub_month, 'target_period':target_period, 'form': form, 'is_edit': False})
    else:
        form = PerformanceForm()
    # new
    return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock_code': stock_code, 'form': form, 'is_edit': False})

def performance_info(request, stock_code, source, pub_year, pub_month, target_period):
    performance = get_object_or_404(Performance, stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period)
    return render(request, 'stock/performance_info.html', {'title': 'Performance Info', 'stock_code': stock_code, 'performance': performance})

def performance_edit(request, stock_code, source, pub_year, pub_month, target_period):
    performance = get_object_or_404(Performance, stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period)
    if request.method == "POST":
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            performance = form.save(commit=False)
            performance.updated_date = timezone.now()
            stock = Stock.objects.get(stock_code=stock_code)
            performance.stock_code = stock
            performance.save()
            # save -> info
            return redirect('performance_info', stock_code=stock_code, source=performance.source, pub_year=performance.pub_year, pub_month=performance.pub_month, target_period=performance.target_period)
        else:
            # not_valid -> edit
            return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock_code': stock_code, 'source':source, 'pub_year': pub_year, 'pub_month': pub_month, 'target_period': target_period, 'form': form, 'is_edit': True})
    else:
        form = PerformanceForm(instance=performance)
        form.fields['source'].widget.attrs['disabled'] = 'disabled'
        form.fields['pub_year'].widget.attrs['disabled'] = 'disabled'
        form.fields['pub_month'].widget.attrs['disabled'] = 'disabled'
        form.fields['target_period'].widget.attrs['disabled'] = 'disabled'
    # edit
    return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock_code': stock_code, 'source': source, 'pub_year': pub_year, 'pub_month': pub_month, 'target_period': target_period, 'form': form, 'is_edit': True})

def performance_delete(request, stock_code, source, pub_year, pub_month, target_period):
    try:
        performance = Performance.objects.get(stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period)
    except Performance.DoesNotExist:
        raise Http404
    performance.delete()
    return redirect('stock_detail', stock_code=stock_code)


# Summary
#----------------------------------
def stock_detail(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    shikiho_latest = Shikiho.objects.filter(stock_code=stock_code).order_by('-pub_year', '-pub_month').first()

    established = Performance.objects.filter(stock_code=stock_code, is_established=True).order_by('target_period')
    latest_target_period = established.last().target_period
    predicted = Performance.objects.filter(stock_code=stock_code, target_period__gt=latest_target_period).order_by('target_period', '-pub_year', '-pub_month', '-source')

    performances_all = established | predicted
    performances_latest = calc_and_set_performance(performances_all)

    return render(request, 'stock/stock_detail.html', {'title': 'Stock Detail', 'stock_code': stock_code, 'stock': stock, 'shikiho_latest': shikiho_latest, 'performances_latest': performances_latest })

def shikiho_all(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    shikihos = Shikiho.objects.filter(stock_code=stock_code).order_by('-pub_year', '-pub_month')

    return render(request, 'stock/shikiho_all.html', {'title': 'Shikiho History', 'stock_code': stock_code, 'stock': stock, 'shikihos': shikihos })

def performance_all(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)

    established = Performance.objects.filter(stock_code=stock_code, is_established=True).order_by('target_period')
    latest_target_period = established.last().target_period
    predicted = Performance.objects.filter(stock_code=stock_code, target_period__gt=latest_target_period).order_by('target_period', '-pub_year', '-pub_month', '-source')

    performances = established | predicted

    return render(request, 'stock/performance_all.html', {'title': 'Performance History', 'stock_code': stock_code, 'stock': stock, 'performances': performances })

# functions
#----------------------------------
def calc_and_set_performance(performances):
    result = []
    previous_period = -1
    pre_sales_amount = -1;
    pre_ordinary_income = -1;
    pre_net_income = -1;

    for performance in performances:
        # Select max (pub_year+pub_month) by target_period
        if ( performance.target_period != previous_period ):
            # Set YoY
            if(pre_sales_amount != -1):
                performance.sales_amount_yoy = (performance.sales_amount  -  pre_sales_amount) / pre_sales_amount
            if (pre_ordinary_income != -1):
                performance.ordinary_income_yoy = (performance.ordinary_income - pre_ordinary_income) / pre_ordinary_income
            if (pre_net_income != -1):
                performance.net_income_yoy = (performance.net_income - pre_net_income) / pre_net_income
            performance.save()
            result.append(performance)

            pre_sales_amount = performance.sales_amount
            pre_ordinary_income = performance.ordinary_income
            pre_net_income = performance.net_income
            previous_period = performance.target_period

    return result