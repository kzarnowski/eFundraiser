from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Fundraiser
from .forms import FundraiserForm


class IndexView(generic.ListView):
    template_name = 'fundraisers/index.html'

    def get_queryset(self):
        return Fundraiser.objects.all().order_by('-start_time')


# def create(request):
#     if request.method == 'POST':
#         form = FundraiserForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/fundraisers')
#     else:
#         form = FundraiserForm()
#
#     return render(request, 'fundraisers/create.html', {'form': form})

class FundraiserCreateView(generic.CreateView):
    model = Fundraiser
    form_class = FundraiserForm
    template_name = 'fundraisers/create.html'

    def form_valid(self, form):
        form.instance.start_time = form.instance.end_time
        form.instance.amount_raised = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fundraisers_index')
