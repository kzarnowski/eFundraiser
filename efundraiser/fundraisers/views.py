from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse_lazy

from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response

from .models import Fundraiser
from .forms import FundraiserForm
from .serializers import FundraiserSerializer


class IndexView(generic.ListView):
    template_name = 'fundraisers/index.html'
    context_object_name = 'fundraisers'
    queryset = Fundraiser.objects.all().order_by('-start_time')


class CreateView(generic.CreateView):
    model = Fundraiser
    form_class = FundraiserForm
    template_name = 'fundraisers/create.html'

    def form_valid(self, form):
        form.instance.start_time = timezone.now()
        form.instance.amount_raised = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fundraisers:index')


class DetailView(generic.DetailView):
    model = Fundraiser
    template_name = 'fundraisers/detail.html'


class FundraiserDeleteView(generic.DeleteView):
    model = Fundraiser
    success_url = reverse_lazy('fundraisers:index')
    template_name = 'fundraisers/delete_confirmation.html'


class FundraiserEditView(generic.edit.UpdateView):
    model = Fundraiser
    fields = ['title', 'description', 'end_time', 'amount_to_raise']
    template_name = 'fundraisers/edit.html'

    def get_success_url(self):
        return reverse_lazy('fundraisers:detail', args=(self.object.pk, ))


# class FundraiserViewSet(GenericViewSet):
#     serializer_class = FundraiserSerializer
#     queryset = Fundraiser.objects.all()
#
#     def list(self, request):
#         serializer = self.get_serializer(data=self.get_queryset, many=True)
#         return Response(serializer.data, template_name='fundraisers/index.html')
#
#     def retrieve(self, request, pk=None):
#         fundraiser = get_object_or_404(self.get_queryset(), pk=pk)
#         serializer = self.get_serializer(data=fundraiser)
#         return Response(serializer.data, template_name='fundraisers/detail.html')
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(serializer)
#
#         return Response(serializer.data, template_name='fundraisers/detail.html')
#
#     def destroy(self, request):
#         fundraiser = self.get_object()
#         fundraiser.delete()
#         return Response(template_name='fundraisers/index.html')

class FundraiserModelViewSet(ModelViewSet):
    serializer_class = FundraiserSerializer
    queryset = Fundraiser.objects.all()
