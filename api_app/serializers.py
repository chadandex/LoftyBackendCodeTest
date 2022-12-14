from rest_framework import serializers
from .models import DogsModel, SomeKeys


class DogsModelSerializer(serializers.ModelSerializer):
    default_value = serializers.IntegerField(default=0)
    description = serializers.CharField(max_length=25)
    imgsrc = serializers.CharField(default='')

    class Meta:
        model = DogsModel
        fields = ('__all__')


class KeysModelSerializer(serializers.ModelSerializer):
    default_value = serializers.IntegerField(default=0)
    name = serializers.CharField(default='')

    class Meta:
        model = SomeKeys
        fields = ('__all__')
