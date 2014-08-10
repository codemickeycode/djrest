from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

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

    # dispatch page
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

'''
@ensure_csrf_cookie
def list_home_view(request):
    template = 'lists/list_base.html'
    context = {}
    return render(request, template, context)
'''