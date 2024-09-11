from celery import shared_task
from info.models import Interface
from .serializers import *

@shared_task
def create_interface(data):
    serializer = InterfaceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        return {"error": serializer.errors}

@shared_task
def update_interface(pk, data):
    try:
        interface = Interface.objects.get(pk=pk)
    except Interface.DoesNotExist:
        return {"error": "Interface not found."}

    serializer = InterfaceSerializer(interface, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    else:
        return {"error": serializer.errors}