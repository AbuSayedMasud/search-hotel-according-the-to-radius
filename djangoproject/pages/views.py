# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def homePageView(request):
#     return HttpResponse("Hello, World!")
# from django.http import HttpResponseRedirect
# from django.shortcuts import render

from django.contrib.gis.geos import Point
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import hotels_Details
from django.contrib.gis.db.models.functions import Distance

from django.contrib.gis.measure import D
class ThankyouPage(TemplateView):
    template_name = "index.html"



class HomePageView(ListView):

   model=hotels_Details.objects.all()
   
   
   
   template_name = "home.html"
   def get_queryset(self):
    # print("hello")
    
    lal=self.request.GET.get("Latitude")
    lon=self.request.GET.get("Longitude")
    radius=self.request.GET.get("Radius")
   
    pnt =Point(float(lon),float(lal),srid=4326)
    print(pnt)
    query = hotels_Details.objects.annotate(distance=Distance('Geopoint', pnt)).order_by('distance').filter(distance__lte=D(km=radius))
    return  query



