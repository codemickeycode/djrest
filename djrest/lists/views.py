from django.shortcuts import render
from django.views.generic import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ListItemGroupSerializer
from .models import ListItemGroup

# Create your views here.
class ListItemGroupLCAPIView(ListCreateAPIView):
    model = ListItemGroup
    serializer_class = ListItemGroupSerializer

class ListItemGroupRUDAPIView(RetrieveUpdateDestroyAPIView):
    model = ListItemGroup
    serializer_class = ListItemGroupSerializer

class ListHomeView(View):
    template_name = 'lists/list_base.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)