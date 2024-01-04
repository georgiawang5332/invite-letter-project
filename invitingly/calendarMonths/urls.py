from django.urls import path

from . import views

app_name = "cale"

# Create your urls here.
urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
]
