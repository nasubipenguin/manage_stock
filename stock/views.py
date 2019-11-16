from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Stock
from .forms import StockForm


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
    return render(request, 'stock/stock_edit.html', {'title': 'Update Stock Info', 'stock_code': stock_code, 'form': form, 'is_edit': True})

def stock_delete(request, stock_code):
    try:
        stock = Stock.objects.get(stock_code=stock_code)
    except Stock.DoesNotExist:
        raise Http404
    stock.delete()
    return redirect('stock_list')

def performance_new(request):
    return render(request, 'stock/performance_edit.html', {})

def performance_info(request, stock_code):
    return render(request, 'stock/performance_info.html', {})

def performance_edit(request, stock_code):
    return render(request, 'stock/performance_edit.html', {})

def shikiho_new(request):
    return render(request, 'stock/shikiho_edit.html', {})

def shikiho_info(request, stock_code):
    return render(request, 'stock/shikiho_info.html', {})

def shikiho_edit(request, stock_code):
    return render(request, 'stock/shikiho_edit.html', {})

def stock_detail(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    return render(request, 'stock/stock_detail.html', {'title': 'Stock Detail', 'stock': stock})