from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='fundraisers_index'),
    # path('create', views.create, name='create')
    path('create', views.FundraiserCreateView.as_view())
]