from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .messaging import publish_event

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("username")
        email = data.get("email")
        publish_event("registered", {"name": name, "email": email})
        user = User.objects.create_user(username=name, email=email,password="123")
        user.save()

        return JsonResponse({"status": f"user registered, id {user.id} "})
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def update_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get("user_id")
        name = data.get("name")
        publish_event("updated", {"user_id": user_id, "name": name})
        return JsonResponse({"status": "user updated"})
    return JsonResponse({"error": "Invalid method"}, status=405)
