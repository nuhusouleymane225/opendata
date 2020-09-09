from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PharmaViewSet

router = DefaultRouter()
router.register('pharmacies', PharmaViewSet, basename='pharmacies')


urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    
]

urlpatterns += router.urls