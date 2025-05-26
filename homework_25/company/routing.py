from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/company/(?P<company_id>\d+)/$', consumers.CompanyConsumer.as_asgi()),
]
