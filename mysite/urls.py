from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from browser_request import views

router = routers.DefaultRouter()
router.register(r'visitors', views.VisitorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.get_client_request_data, name='landing_page'),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
