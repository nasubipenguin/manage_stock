from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import Http404
from .models import Stock, Shikiho
from .forms import StockForm, ShikihoForm


# Stock
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
            return redirect('stock_info', stock_code=stock.stock_code)
        else:
            return render(request, 'stock/stock_edit.html', {'title': 'Register Stock Info', 'form': form})
    else:
        form = StockForm()
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
            return redirect('stock_info', stock_code=stock.stock_code)
    else:
        form = StockForm(instance=stock)
        form.fields['stock_code'].widget.attrs['disabled'] = 'disabled'
    return render(request, 'stock/stock_edit.html', {'title': 'Update Stock Info', 'stock_code': stock_code, 'form': form, 'is_edit': True})

def stock_delete(request, stock_code):
    try:
        stock = Stock.objects.get(stock_code=stock_code)
    except Stock.DoesNotExist:
        raise Http404
    stock.delete()
    return redirect('stock_list')

# Performance
def performance_new(request, stock_code):
    return render(request, 'stock/performance_edit.html', {})

def performance_info(request, stock_code, pub_year, pub_month, target_period):
    return render(request, 'stock/performance_info.html', {})

def performance_edit(request, stock_code, pub_year, pub_month, target_period):
    return render(request, 'stock/performance_edit.html', {})

def performance_delete(request, stock_code, pub_year, pub_month):
    return redirect('performance_info', stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)

# Shikiho
def shikiho_new(request, stock_code):
    if request.method == "POST":
        form = ShikihoForm(request.POST)
        if form.is_valid():
            shikiho = form.save(commit=False)
            shikiho.updated_date = timezone.now()
            stock = Stock.objects.get(stock_code=stock_code)
            shikiho.stock_code = stock
            shikiho.save()
            return redirect('shikiho_info', stock_code=stock_code, pub_year=shikiho.pub_year, pub_month=shikiho.pub_month)
        else:
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'form': form})
    else:
        form = ShikihoForm()
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
            return redirect('shikiho_info', stock_code=stock_code, pub_year=shikiho.pub_year, pub_month=shikiho.pub_month)
        else:
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'pub_year': pub_year, 'pub_month': pub_month, 'form': form})
    else:
        form = ShikihoForm(instance=shikiho)
    return render(request, 'stock/shikiho_edit.html', {'title': 'Register Shikiho Info', 'stock_code': stock_code, 'pub_year': pub_year, 'pub_month': pub_month, 'form': form, 'is_edit': True})

def shikiho_delete(request, stock_code, pub_year, pub_month):
    try:
        #stock = Stock.objects.get(stock_code=stock_code)
        shikiho = Shikiho.objects.get(stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    except Shikiho.DoesNotExist:
        raise Http404
    shikiho.delete()
    return redirect('stock_detail', stock_code=stock_code)

# Summary
def stock_detail(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    return render(request, 'stock/stock_detail.html', {'title': 'Stock Detail', 'stock': stock})