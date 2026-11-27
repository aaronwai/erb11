from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.all().filter(is_published=True).order_by("-list_date")
    paginator = Paginator(listings, 3)
    page_number = request.GET.get("page")
    paged_listings = paginator.get_page(page_number)
    current_time = timezone.localtime().time()
    context = {"listings": paged_listings, "current_time": current_time}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    current_time = timezone.localtime().time()
    context = {"listing": listing, "current_time": current_time}
    return render(request, "listings/listing.html", context)
