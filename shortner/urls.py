from django.urls import path
from .views import ShortURLViewSet

shortener = ShortURLViewSet.as_view({
    'post': 'create',
})

urlpatterns = [
    path('shorten', shortener),
    path('shorten/<str:pk>', ShortURLViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('shorten/<str:pk>/stats', ShortURLViewSet.as_view({
        'get': 'stats'
    })),
]