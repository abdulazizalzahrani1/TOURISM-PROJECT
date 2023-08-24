from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('city/riyadh/', views.riyadh_view, name="riyadh_view"),
    path('city/makkah/', views.makkah_view, name="makkah_view"),
    path('city/baha/', views.baha_view, name="baha_view"),
    path('city/dammam/', views.dammam_view, name="dammam_view"),

]
