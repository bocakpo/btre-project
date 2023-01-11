from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    Listings = Listing.objects.order_by('-listing_date').filter(is_published=True)[:3]
    context = {'listings': Listings}
    return render(request, 'pages/index.html', context)

def about(request):
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    realtors = Realtor.objects.all()
    context = {'realtors': realtors, 'mvp_realtor': mvp_realtors}
    return render(request, 'pages/about.html', context)