from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view', views.HellowApiView.as_view()),
    path('', include(router.urls))
]