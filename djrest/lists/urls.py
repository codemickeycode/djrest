from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListItemGroupLCAPIView, ListItemGroupRUDAPIView, ListHomeView

api_patterns = format_suffix_patterns(patterns(
    '',
    url(r'^lists$', ListItemGroupLCAPIView.as_view(), name='list_item_group'),
    url(r'^lists/(?P<pk>\d+)$', ListItemGroupRUDAPIView.as_view(), name='list_item_group_details'),
))

urlpatterns = patterns(
    '',
    url(r'^lists/', ListHomeView.as_view()),
    url(r'^api/', include(api_patterns), name='lists_api'),
)