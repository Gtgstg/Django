
from django.conf.urls import url,include
from django.contrib import admin
import demo.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include("demo.urls")),
]
