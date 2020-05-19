from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from .models import Listing

# Create your views here.

def index(request):
    # fetching data from database
    # - sign indecates descending order
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # if i got to another id page then 404 page should display
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')