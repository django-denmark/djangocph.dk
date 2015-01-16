from django.conf.urls import patterns, include, url
from django.contrib import admin
from djangocph import views
urlpatterns = patterns('',
    url(r'^$', views.Website.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
