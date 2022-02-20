from django.shortcuts import render
from django.views import generic

from .models import Fundraiser

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'fundraisers/index.html'

    def get_queryset(self):
        return Fundraiser.objects.all().order_by('-start_time')