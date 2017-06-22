# -*- coding: utf-8 -*-
#pylint --disable=E1101
from __future__ import unicode_literals

from django.shortcuts import render
# from .models import Products
from .models import Bikes
# Create your views here.
def index(request):
    bikes = Bikes.objects.all()
    print "*"*50
    print (bikes)
    print "*"*50
    Bikes.objects.create(name="Ninja",
    description="The Kawasaki Ninja is the trademarked name of several series of Kawasaki sport bikes, that started with the 1984 GPZ900R. ",
    weight="455.1",
    price="5999.99",
    cost="4000.00",
    ridecategory="Sports")

    Bikes.objects.create(name="Vulcan",
    description="Kawasaki Vulcan is the trademarked name of several series of Kawasaki cruiser bikes.",
    weight="655.1",
    price="15999.99",
    cost="14000.00",
    ridecategory="Cruiser")
    
    Bikes.objects.create(name="Mule",
    description="Kawasaki Mule is the trademarked name of several series of Kawasaki work utility vehicles and ATV bikes.",
    weight="255.1",
    price="7999.99",
    cost="5000.00",
    ridecategory="ATV")
    bikes = Bikes.objects.all()
    print "!"*50
    print (bikes)
    print "!"*50
    return render(request, 'inv/index.html')