from rest_framework import serializers
from .models import ListItemGroup

class ListItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItemGroup
        fields = ('id','title',)
