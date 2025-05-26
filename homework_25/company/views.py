from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Company
from django.shortcuts import render

def notify_company(request, company_id):
    message = "Company data has been updated."

    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        f"company_{company_id}",
        {
            "type": "company_message",
            "message": message,
            "user": "system"
        }
    )
    return JsonResponse({"status": "sent"})



def index(request):
    is_auth = request.user.is_authenticated
    return render(request, 'chat1.html', {'is_auth': is_auth})