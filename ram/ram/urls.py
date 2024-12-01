from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('powercalc/', views.calculate_power, name="powercalc"),
    path('', views.calculate_power, name="powercalcroot"),  # This will map the root URL to the same view
]


