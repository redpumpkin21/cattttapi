from .models import Cat
from rest_framework import serializers

## Create a Serializer for Our Model
class CatSerializer(serializers.HyperlinkedModelSerializer):
    # nest a Meta class to configure the serializer
    class Meta:
        # which model does it serialize
        model = Cat
        # which fields should be serialized
        fields = ["id", "name", "description", "image"]