# urls.py
# from rest_framework.routers import DefaultRouter
# from .views import CustomerMessageViewSet

# router = DefaultRouter()
# router.register(r'your-models', CustomerMessageViewSet, basename='CustomerMessage')
# urlpatterns = router.urls
from django.urls import path
from Messages import views

urlpatterns = [
    path('message/', views.MessageApiView.as_view(), name='message'),
    path('element/<int:id>/',views.ElementApiView.as_view(), name='element'),
]