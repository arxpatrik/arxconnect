from django.urls import path
from . import views

app_name = "dashboards"
urlpatterns = [
    path("bi/", views.dashboards_view, name="power_bi")
]