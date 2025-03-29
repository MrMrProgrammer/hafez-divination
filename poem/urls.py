from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.PoemApiView)

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('divination/', views.DivinationView.as_view(), name='divination'),
    path('api/divination/', views.DivinationApiView.as_view()),
    path('api/', include(router.urls)),
]