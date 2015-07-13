from django.conf.urls import patterns, include, url
from core.views import coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view())),
    url(r'location$', coreviews.LocationListView.as_view())),
]