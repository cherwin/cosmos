from django.shortcuts import render
from django.http import HttpResponseNotAllowed

# Create your views here.
def landing_page(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    return render(request, "landing_page.html")
