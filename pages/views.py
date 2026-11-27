from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone

from accounts.models import Staff
from listings.choices import cuisine_choices, district_choices, price_choices
from listings.models import Listing


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
    staffs = Staff.objects.order_by("-hire_date")[:3]
    features = Staff.objects.filter(is_promo=True)
    context = {"staffs": staffs, "features": features}
    return render(request, "pages/about.html", context)


def search(request):
    current_time = timezone.localtime().time()
    queryset_list = Listing.objects.order_by("-list_date")
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(
                Q(description__icontains=keywords) | Q(title__icontains=keywords)
            )
    if "district" in request.GET:
        district = request.GET["district"]
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if "cuisine" in request.GET:
        cuisine = request.GET["cuisine"]
        if cuisine:
            queryset_list = queryset_list.filter(cuisine_choices__iexact=cuisine)
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            if price == "Budget":
                queryset_list = queryset_list.filter(price__lte=200)
            if price == "Average":
                queryset_list = queryset_list.filter(price__gt=200).filter(
                    price__lte=400
                )
            if price == "Premium":
                queryset_list = queryset_list.filter(price__gt=400)
    if "open" in request.GET:
        open = request.GET["open"]
        if open == "Yes":
            queryset_list = queryset_list.filter(opening_hours__lte=current_time)
        if open == "No":
            queryset_list = queryset_list.filter(opening_hours__gte=current_time)
    paginator = Paginator(queryset_list, 3)
    page_number = request.GET.get("page")
    paged_listings = paginator.get_page(page_number)
    get_params = request.GET.copy()
    get_params.pop("page", None)
    get_params = get_params.urlencode()
    context = {
        "listings": paged_listings,
        "current_time": current_time,
        "district_choices": district_choices,
        "cuisine_choices": cuisine_choices,
        "price_choices": price_choices,
        "values": request.GET,
        "get_params": get_params,
    }
    return render(request, "pages/search.html", context)
