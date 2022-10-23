import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import user_table, device_smart, consumption_calc, treek
from .serializers import ConsumptionSerializer, TreekSerializer, DevicesSerializer
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse("This works!")
    


#@csrf_exempt
def carbonfootprint_calculation(request):
    if request.method == "GET":
        date = datetime.today()
        month = date.strftime('%m')
        year = date.strftime('%Y')
        data = consumption_calc.objects.filter(created_date__year__gte=year,
                              created_date__month__gte=month,
                              created_date__year__lte=year,
                              created_date__month__lte=month)
        data = ConsumptionSerializer(data, many=True)
        data = json.loads(json.dumps(data.data))
        elec =0
        mileage = 0
        for i in data:
            elec += i['electricty_consumption']
            mileage += i['mileage']
        carbon = ((elec/1000)*0.7080) + (mileage * 0.79)
        trees = carbon // 0.16
        devices = device_smart.objects.filter(user_id = user_table.objects.get(id=1))
        devices = DevicesSerializer(devices, many=True)
        result = {
            "consumption": carbon,
            "trees": trees,
            "months" :["August", "September","October"],
            "datapoints":[330, 350, carbon],
            "devices": json.loads(json.dumps(devices.data))
        }
        return HttpResponse(json.dumps(result), content_type="application/json")

def treek_calculation(request):
    if request.method == "GET":
        data = treek.objects.all()
        data = TreekSerializer(data, many=True)
        
        return HttpResponse(json.dumps(data.data), content_type="application/json")





