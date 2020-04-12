#its for JSOn send data to the ML model in JS form

from rest_framework import serializers
from calc.models import diabetes
from calc.models import heart

class diabetesSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model=diabetes
            fields='__all__'


class heartSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            model=heart
            fields='__all__'
