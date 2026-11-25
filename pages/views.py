from django.shortcuts import render
from listings.models import Listing
from django.utils import timezone


# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    current_time = timezone.localtime().time()
    context = {"listings": listings, "current_time": current_time}
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")
