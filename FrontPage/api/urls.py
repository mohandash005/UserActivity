from django.conf.urls import url
from django.contrib import admin
from .views import PostDetailAPIView, PostListAPIView

urlpatterns = [
    url(r'$', PostListAPIView.as_view(), name='List'),
    url(r'(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail')
]
