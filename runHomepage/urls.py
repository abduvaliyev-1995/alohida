from django.urls import path
from .views import homepage, HomePageView, AboutPageView, DetailPageView, BlogsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('blogs/', BlogsPageView.as_view(), name = 'blogs'),
    path('details/', DetailPageView.as_view(), name = 'details'),
]
