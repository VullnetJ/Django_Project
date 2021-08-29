from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from .models import Pages


# Create your views here.

def index(request):
    pages = Pages.objects.order_by('-list_date').filter(is_published=True)  # this show if is published when you
    # activate the check button.
    pages = Pages.objects.order_by('-list_date').filter(is_published=True)[:3]
    paginator = Paginator(pages, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'pages': paged_listings
    }

    return render(request, 'pages/index.html', context)  # {
    # 'name': 'Vullnet'
    # } another method to call the name
    # )


def about(request):
    return render(request, 'pages/about.html')
