from django.conf.urls import url
from .views import about_me, articles, article

urlpatterns = [
    url(r'^about-me/', about_me),
    url(r'^$', articles),
    url(r'^article/(?P<id>\d+)/$', article)
]
