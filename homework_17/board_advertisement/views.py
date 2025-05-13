from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Category
from django.shortcuts import render
from django.views.generic import ListView

from .models import Advertisement


class UserAdsView(ListView):
    model = Advertisement
    template_name = 'user_ads.html'
    context_object_name = 'ads'
    queryset = Advertisement.objects.all()

    def get_queryset(self):
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)
        ads = Advertisement.objects.filter(
            created_at__gte=thirty_days_ago
        )

        return ads


def ads_by_category(request, category_id):
    category = Category.objects.filter(id=category_id)
    ads = Advertisement.objects.filter(category_id=category_id)
    return render(request, 'category.html', {'category': category, 'ads': ads})
