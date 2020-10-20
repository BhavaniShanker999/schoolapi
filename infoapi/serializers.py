from rest_framework import serializers
from .models import *

class school_serializer(serializers.ModelSerializer):
    class Meta:
        model= school_model
        fields=('Name','Branches','Total_staff')
class staff_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= staff_model
        fields=('Name','Gender','Present_salary','Subjects','url')