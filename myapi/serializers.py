'''
We need to tell REST Framework about our Hero model and how it should serialize the data.

The process of querying and converting tabular database
values into JSON or another format is called serialization.
'''
from rest_framework import serializers
from .models import Hero


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')
