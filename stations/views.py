from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from stations.models import Company, Station


def hello(request):
    return HttpResponse("Hello World")


def company_name(request, company_id):
    # company = Company.objects.get(pk=company_id)
    company = get_object_or_404(Company, pk=company_id)
    return HttpResponse("<h1>Company " + company_id + " is " + company.name + "</h1>")


def company_index(request):
    companies = Company.objects.all().order_by("name")
    return render(request, "company_index.html", {'companies': companies})
    # render - pozadavek pouzit template
    # predavaji se parametry request - nas request, druhy param je nazev souboru s templatem
    # posledni parametr je slovnik, klic je nazev promenne v templatu, value je promenna z view


def station_index(request):
    stations = Station.objects.all().order_by("name")
    return render(request, "stations_index.html", {'stations': stations})
