# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

from stock.models import Stock

def stock_list(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks,}
    return render(request, 'stocks.html', context)

# Create your views here.
