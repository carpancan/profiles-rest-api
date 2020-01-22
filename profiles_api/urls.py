from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewset)

urlpatterns = [
    path('hello-view', views.HellowApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]