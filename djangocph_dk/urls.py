from django.conf.urls import include, url
from django.contrib import admin
from djangocph import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='home'),
]
