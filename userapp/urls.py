from django.urls import path

from userapp.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]