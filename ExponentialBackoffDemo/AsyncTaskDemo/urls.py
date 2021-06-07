from django.urls import include, path
from rest_framework import routers
from . import views




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('calc_mystery',views.calculateMystery.as_view()),
    path('check_mystery',views.checkMystery.as_view())

]