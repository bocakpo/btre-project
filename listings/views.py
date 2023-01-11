from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    listing = Listing.objects.order_by('-listing_date').filter(is_published=True)
    paginator = Paginator(listing, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'listings': page}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listings = get_object_or_404(Listing, id=listing_id)
    context = {'listings': listings}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')