from rest_framework import serializers
from consumption.models import user_table, device_smart,consumption_calc,treek


class ConsumptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = consumption_calc
        fields = ('id',
                  'user_id',
                  'device_id',
                  'electricty_consumption',
                  'mileage',
                  'number_of_trees',
                  'family_members',
                  'created_date')

class TreekSerializer(serializers.ModelSerializer):
    class Meta:
        model = treek
        fields = ('id',
                  'user_id',
                  'progress',
                  'goal',
                  'month',)

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = device_smart
        fields = ('id',
                  'device_name',
                  'user_id',
                  'device_type',
                  'imgurl',
                  'status',)