from cities_light.models import Country, Region, City
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt



def home(request):
    country = Country.objects.all()
    region = Region.objects.all()
    city = City.objects.all()
    return render(request, 'home/country.html',{"country":country, 'region':region, 'city':city})



def getregion(request, contryid):
    country = Country.objects.get(id=int(contryid))
    region = Region.objects.filter(country = country)
    html = render_to_string('home/region.html',{'region':region })
    return HttpResponse(html, content_type='application/html')

def getrcity(request, regionid):
    print "inside views"
    #country = Country.objects.get(id=int(regionid))
    region = Region.objects.get(id = int(regionid))
    city = City.objects.filter(region=region)
    print city
    html = render_to_string('home/city.html',{'city':city })
    return HttpResponse(html, content_type='application/html')