import math

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import Http404
from .models import Stock, Shikiho, Performance, Note
from .forms import StockForm, ShikihoForm, PerformanceForm, NoteForm


# Stock List
#----------------------------------
def stock_list(request):
    stocks = Stock.objects.filter(updated_date__lte=timezone.now())
    # if request.GET.get('watch_flag'):
    #     stocks = stocks.filter(watch_flag__exact=request.GET.get('watch_flag'))
    if request.GET.get('stock_code'):
        stocks = stocks.filter(stock_code__exact=request.GET.get('stock_code'))
    if request.GET.get('stock_name'):
        stocks = stocks.filter(stock_name__contains=request.GET.get('stock_name'))
    stocks = stocks.order_by('accounting_month', 'stock_code')

    watching = []
    considering = []
    unwatching = []
    for stock in stocks:
        latest_notes = ''
        latest_notes_date = ''
        note = Note.objects.filter(stock_code=stock.stock_code).order_by('-publish_date').first()
        if( note != None and note.summary != None ):
            latest_notes = note.summary
            latest_notes_date = note.publish_date
        new_stock = {'stock_code':stock.stock_code, 'stock_name':stock.stock_name, 'accounting_month':stock.accounting_month, 'latest_notes':latest_notes, 'latest_notes_date':latest_notes_date, 'watch_flag':stock.watch_flag}
        if( stock.watch_flag == 1):
            watching.append(new_stock)
        elif( stock.watch_flag == 2):
            considering.append(new_stock)
        else:
            unwatching.append(new_stock)

    return render(request, 'stock/stock_list.html', {'title': 'Stock List', 'watching': watching, 'considering': considering, 'unwatching': unwatching})


# Stock
#----------------------------------
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
            return render(request, 'stock/stock_edit.html', {'title': 'Register Stock Info', 'form': form, 'is_edit': True})
    else:
        form = StockForm(instance=stock)
        form.fields['stock_code'].widget.attrs['disabled'] = 'disabled'
    # edit
    return render(request, 'stock/stock_edit.html', {'title': 'Update Stock Info', 'form': form, 'is_edit': True})

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
    stock = Stock.objects.get(stock_code=stock_code)
    if request.method == "POST":
        form = ShikihoForm(request.POST)
        pub_year = request.POST['pub_year']
        pub_month = request.POST['pub_month']
        if Shikiho.objects.filter(stock_code=stock_code, pub_year=pub_year, pub_month=pub_month).exists():
            # duplicate -> edit
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Quarterly Info', 'stock': stock, 'form': form, 'exists': True})
        if form.is_valid():
            shikiho = form.save(commit=False)
            shikiho.updated_date = timezone.now()
            shikiho.stock_code = stock
            shikiho.save()
            # save -> info
            return redirect('shikiho_info', stock_code=stock_code, pub_year=shikiho.pub_year, pub_month=shikiho.pub_month)
        else:
            # not_valid -> new
            return render(request, 'stock/shikiho_edit.html', {'title': 'Register Quarterly Info', 'stock': stock, 'form': form, 'is_edit': False})
    else:
        form = ShikihoForm()
    # new
    return render(request, 'stock/shikiho_edit.html', {'title': 'Register Quarterly Info', 'stock': stock, 'form': form, 'is_edit': False})

def shikiho_info(request, stock_code, pub_year, pub_month):
    shikiho = get_object_or_404(Shikiho, stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    return render(request, 'stock/shikiho_info.html', {'title': 'Quarterly Info', 'shikiho': shikiho})

def shikiho_edit(request, stock_code, pub_year, pub_month):
    stock = Stock.objects.get(stock_code=stock_code)
    shikiho = get_object_or_404(Shikiho, stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    if request.method == "POST":
        form = ShikihoForm(request.POST, instance=shikiho)
        if form.is_valid():
            shikiho = form.save(commit=False)
            shikiho.updated_date = timezone.now()
            shikiho.stock_code = stock
            shikiho.save()
            # save -> info
            return redirect('shikiho_info', stock_code=stock_code, pub_year=shikiho.pub_year, pub_month=shikiho.pub_month)
        else:
            # not_valid -> edit
            return render(request, 'stock/shikiho_edit.html', {'title': 'Update Quarterly Info', 'stock': stock, 'form': form, 'is_edit': True})
    else:
        form = ShikihoForm(instance=shikiho)
        form.fields['pub_year'].widget.attrs['disabled'] = 'disabled'
        form.fields['pub_month'].widget.attrs['disabled'] = 'disabled'
    # edit
    return render(request, 'stock/shikiho_edit.html', {'title': 'Update Quarterly Info', 'stock': stock, 'form': form, 'is_edit': True})

def shikiho_delete(request, stock_code, pub_year, pub_month):
    try:
        shikiho = Shikiho.objects.get(stock_code=stock_code, pub_year=pub_year, pub_month=pub_month)
    except Shikiho.DoesNotExist:
        raise Http404
    shikiho.delete()
    return redirect('stock_detail', stock_code=stock_code)

def shikiho_all(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    shikihos = Shikiho.objects.filter(stock_code=stock_code).order_by('-pub_year', '-pub_month')

    if (len(shikihos) == 0):
        shikihos = None

    return render(request, 'stock/shikiho_all.html', {'title': 'Quarterly History', 'stock': stock, 'shikihos': shikihos })


# Performance
#----------------------------------
def performance_new(request, stock_code):
    stock = Stock.objects.get(stock_code=stock_code)
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        stock_code = request.POST['stock_code']
        source = request.POST['source']
        pub_year = request.POST['pub_year']
        pub_month = request.POST['pub_month']
        target_period = request.POST['target_period']
        if Performance.objects.filter(stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period).exists():
            # duplicate -> edit
            return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock': stock, 'form': form, 'exists': True})
        if form.is_valid():
            performance = form.save(commit=False)
            performance.updated_date = timezone.now()
            performance.stock_code = stock
            performance.save()
            # save -> info
            return redirect('performance_info', stock_code=stock_code, source=performance.source, pub_year=performance.pub_year, pub_month=performance.pub_month, target_period=target_period)
        else:
            # not_valid -> new
            return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock': stock, 'form': form, 'is_edit': False})
    else:
        form = PerformanceForm()
    # new
    return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock': stock, 'form': form, 'is_edit': False})

def performance_info(request, stock_code, source, pub_year, pub_month, target_period):
    stock = Stock.objects.get(stock_code=stock_code)
    performance = get_object_or_404(Performance, stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period)
    return render(request, 'stock/performance_info.html', {'title': 'Performance Info', 'stock': stock, 'performance': performance})

def performance_edit(request, stock_code, source, pub_year, pub_month, target_period):
    stock = Stock.objects.get(stock_code=stock_code)
    performance = get_object_or_404(Performance, stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period)
    if request.method == "POST":
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            performance = form.save(commit=False)
            performance.updated_date = timezone.now()
            performance.stock_code = stock
            performance.save()
            # save -> info
            return redirect('performance_info', stock_code=stock_code, source=performance.source, pub_year=performance.pub_year, pub_month=performance.pub_month, target_period=performance.target_period)
        else:
            # not_valid -> edit
            return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock': stock, 'form': form, 'is_edit': True})
    else:
        form = PerformanceForm(instance=performance)
        form.fields['source'].widget.attrs['disabled'] = 'disabled'
        form.fields['pub_year'].widget.attrs['disabled'] = 'disabled'
        form.fields['pub_month'].widget.attrs['disabled'] = 'disabled'
        form.fields['target_period'].widget.attrs['disabled'] = 'disabled'
    # edit
    return render(request, 'stock/performance_edit.html', {'title': 'Register Performance Info', 'stock': stock, 'form': form, 'is_edit': True})

def performance_delete(request, stock_code, source, pub_year, pub_month, target_period):
    try:
        performance = Performance.objects.get(stock_code=stock_code, source=source, pub_year=pub_year, pub_month=pub_month, target_period=target_period)
    except Performance.DoesNotExist:
        raise Http404
    performance.delete()
    return redirect('stock_detail', stock_code=stock_code)

def performance_all(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)

    established = Performance.objects.filter(stock_code=stock_code, is_established=True).order_by('target_period')
    predicted = Performance.objects.filter(stock_code=stock_code).order_by('target_period', 'pub_year', 'pub_month', 'source')
    if (established.count() > 0):
        latest_target_period = established.last().target_period
        predicted = predicted.filter(target_period__gt=latest_target_period)

    performances = established | predicted
    if( len(performances) == 0 ):
        performances = None

    return render(request, 'stock/performance_all.html', {'title': 'Performance History', 'stock': stock, 'performances': performances })


# Note
#----------------------------------
def note_new(request, stock_code):
    stock = Stock.objects.get(stock_code=stock_code)
    if request.method == "POST":
        form = NoteForm(request.POST)
        stock_code = request.POST['stock_code']
        if form.is_valid():
            note = form.save(commit=False)
            note.updated_date = timezone.now()
            note.stock_code = stock
            note.save()
            # save -> info
            id = note.id
            return redirect('note_info', stock_code=stock_code, id=id)
        else:
            # not_valid -> new
            return render(request, 'stock/note_edit.html', {'title': 'Register Note', 'stock': stock, 'form': form, 'is_edit': False})
    else:
        form = NoteForm()
    # new
    return render(request, 'stock/note_edit.html', {'title': 'Register Note', 'stock': stock, 'form': form, 'is_edit': False})

def note_info(request, stock_code, id):
    stock = Stock.objects.get(stock_code=stock_code)
    note = get_object_or_404(Note, stock_code=stock_code, id=id)
    return render(request, 'stock/note_info.html', {'title': 'Notes', 'stock': stock, 'note': note})

def note_edit(request, stock_code, id):
    stock = Stock.objects.get(stock_code=stock_code)
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.updated_date = timezone.now()
            note.stock_code = stock
            note.save()
            # save -> info
            return redirect('note_info', stock_code=stock_code, id=id)
        else:
            # not_valid -> edit
            return render(request, 'stock/note_edit.html', {'title': 'Update Note', 'stock': stock, 'id':id ,'form': form, 'is_edit': True})
    else:
        form = NoteForm(instance=note)
    # edit
    return render(request, 'stock/note_edit.html', {'title': 'Update Note', 'stock': stock, 'id':id , 'form': form, 'is_edit': True})

def note_delete(request, stock_code, id):
    try:
        note = Note.objects.get(stock_code=stock_code, id=id)
    except Note.DoesNotExist:
        raise Http404
    note.delete()
    return redirect('stock_detail', stock_code=stock_code)

def note_all(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    notes = Note.objects.filter(stock_code=stock_code).order_by('-publish_date')

    if (len(notes) == 0):
        notes = None

    return render(request, 'stock/note_all.html', {'title': 'Note History', 'stock': stock, 'notes': notes })


# Summary
#----------------------------------
def stock_detail(request, stock_code):
    stock = get_object_or_404(Stock, stock_code=stock_code)
    note_latest = Note.objects.filter(stock_code=stock_code).order_by('-publish_date').first()
    shikiho_latest = Shikiho.objects.filter(stock_code=stock_code).order_by('-pub_year', '-pub_month').first()

    established = Performance.objects.filter(stock_code=stock_code, is_established=True).order_by('target_period')
    predicted = Performance.objects.filter(stock_code=stock_code).order_by('target_period', '-pub_year', '-pub_month', '-source')
    if( established.count() > 0 ):
        latest_target_period = established.last().target_period
        predicted = predicted.filter(target_period__gt=latest_target_period)

    performances_all = established | predicted
    performance_latest = calc_and_set_performance(performances_all)
    if( len(performance_latest) == 0 ):
        performance_latest = None

    return render(request, 'stock/stock_detail.html', {'title': 'Stock Summary', 'stock_code': stock_code, 'stock': stock, 'note_latest': note_latest, 'shikiho_latest': shikiho_latest, 'performance_latest': performance_latest })


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

