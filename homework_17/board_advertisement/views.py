from datetime import timedelta

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from .models import Advertisement, Category


class UserAdsView(ListView):
    """
    Представление для отображения объявлений, созданных за последние 30 дней.
    """
    model = Advertisement
    template_name = 'user_ads.html'
    context_object_name = 'ads'
    queryset = Advertisement.objects.all()

    def get_queryset(self) -> QuerySet:
        """
        Возвращает объявления, созданные не более 30 дней назад.
        """
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)
        ads = Advertisement.objects.filter(created_at__gte=thirty_days_ago)
        return ads


def ads_by_category(request: HttpRequest, category_id: int) -> HttpResponse:
    """
    Представление для отображения объявлений по категории.

    Args:
        request: HTTP-запрос.
        category_id: Идентификатор категории.

    Returns:
        HTTP-ответ с отрендеренным шаблоном и объявлениями данной категории.
    """
    category = get_object_or_404(Category, id=category_id)
    ads = Advertisement.objects.filter(category_id=category_id)
    return render(request, 'category.html', {'category': category, 'ads': ads})
