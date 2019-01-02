from django.shortcuts import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_command(req):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('events', {'type': 'events_listener'})
    return HttpResponse('<p>Done</p>')
