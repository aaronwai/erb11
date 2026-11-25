from django.shortcuts import render
from listings.models import Listing
from django.utils import timezone
from listings.choices import district_choices, cuisine_choices, price_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    current_time = timezone.localtime().time()
    context = {
        "listings": listings,
        "current_time": current_time,
        "district_choices": district_choices,
        "cuisine_choices": cuisine_choices,
        "price_choices": price_choices,
    }
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")


def search(request):
    return render(request, "pages/search.html")
