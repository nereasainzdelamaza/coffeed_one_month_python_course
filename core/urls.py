from django.conf.urls import patterns, include, url
from core.views import coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view())),
]