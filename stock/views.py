from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Stock
from .forms import StockForm

def stock_list(request):
    stocks = Stock.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stock/stock_list.html', {'stocks': stocks})

def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.published_date = timezone.now()
            stock.save()
            return redirect('stock_info', pk=stock.pk)
    else:
        form = StockForm()
    return render(request, 'stock/stock_edit.html', {'form': form})

def stock_info(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stock/stock_info.html', {'stock': stock})

def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.published_date = timezone.now()
            stock.save()
            return redirect('stock_info', pk=stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'stock/stock_edit.html', {'form': form})

def performance_new(request):
    return render(request, 'stock/performance_edit.html', {})

def performance_info(request, pk):
    return render(request, 'stock/performance_info.html', {})

def performance_edit(request, pk):
    return render(request, 'stock/performance_edit.html', {})

def shikiho_new(request):
    return render(request, 'stock/shikiho_edit.html', {})

def shikiho_info(request, pk):
    return render(request, 'stock/shikiho_info.html', {})

def shikiho_edit(request, pk):
    return render(request, 'stock/shikiho_edit.html', {})

def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stock/stock_detail.html', {'stock': stock})