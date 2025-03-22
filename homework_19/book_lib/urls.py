from rest_framework.routers import DefaultRouter
from book_lib.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = []
urlpatterns += router.urls
