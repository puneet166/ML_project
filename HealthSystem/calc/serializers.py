#its for JSOn send data to the ML model in JS form

from rest_framework import serializers
from calc.models import diabetes

class diabetesSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model=diabetes
            fields='__all__'
