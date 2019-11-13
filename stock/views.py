from django.shortcuts import render
from .models import Stock, Performance, Shikiho

def stock_list(request):
    return render(request, 'blog/stock_list.html', {})

def stock_new(request):
    return render(request, 'blog/stock_new.html', {})

def stock_info(request):
    return render(request, 'blog/stock_info.html', {})

def stock_edit(request):
    return render(request, 'blog/stock_edit.html', {})

def stock_detail(request):
    return render(request, 'blog/stock_detail.html', {})

def performance_new(request):
    return render(request, 'blog/performance_new.html', {})

def performance_info(request):
    return render(request, 'blog/performance_info.html', {})

def performance_edit(request):
    return render(request, 'blog/performance_edit.html', {})

def shikiho_new(request):
    return render(request, 'blog/shikiho_new.html', {})

def shikiho_info(request):
    return render(request, 'blog/shikiho_info.html', {})

def shikiho_edit(request):
    return render(request, 'blog/shikiho_edit.html', {})
