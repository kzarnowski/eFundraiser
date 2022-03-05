from django.urls import path
from . import views

app_name = 'fundraisers'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.FundraiserDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', views.FundraiserEditView.as_view(), name='edit'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]