from django.urls import path

from board_advertisement import views
from board_advertisement.views import UserAdsView, ads_by_category

urlpatterns = [
    path('ads/recent/', UserAdsView.as_view(), name='recent_ads'),
    path('ads/category/<int:category_id>/', views.ads_by_category, name='ads_by_category'),
    # path('my-ads/', views.UserAdsView.as_view(), name='user_ads'),
]
