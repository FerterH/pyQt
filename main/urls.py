from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage),
    path('europe', views.europe),
    path('asia', views.asia),
    path('america', views.america),
    path('russia', views.russia),



]