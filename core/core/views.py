from django.shortcuts import render
from django.http import HttpResponseNotAllowed

from newsletter.views import SubscribeRequestView

# Create your views here.
def landing_page(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    return render(request, "core/landing_page.html")
