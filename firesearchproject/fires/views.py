from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import folium
# Create your views here.

from .models import Fire
 
 
class HomePageView(TemplateView):
    template_name = 'home.html'
 
class SearchResultsView(ListView):
    model = Fire
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        query1 = self.request.GET.get('q1')
        object_list =  Fire.objects.filter(
            Q(date__icontains=query),
            Q(type_id = query1)
        )
        m=folium.Map()
        for fire in object_list:
            folium.Marker([fire.lat, fire.lon]).add_to(map)

        context ={
            'map': map,
        }
        return object_list
