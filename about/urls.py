from django.urls import path
from .views import AboutUsView


# Urls for the about us page
urlpatterns = [
    path('about/', AboutUsView.as_view(), name='about'),
    path('about', AboutUsView.as_view()),
]
