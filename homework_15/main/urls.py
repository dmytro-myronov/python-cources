from django.urls import path, re_path

from . import views
from .views import home, about, ContactView, ServiceView

urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServiceView.as_view(), name='services'),
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post_view'),
    re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view, name='profile_view'),
]

