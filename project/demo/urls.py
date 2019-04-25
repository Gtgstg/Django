'''
how to include different differnt app & how to include it
'''
from django.conf.urls import url
import demo.views
app_name='demo'

urlpatterns = [
    url(r'^$',demo.views.index,name='index'),
    url(r'^about/$',demo.views.about,name='about'),
    url(r'^login/$',demo.views.login,name='login'),
    url(r'^auth/$',demo.views.auth_view,name='auth_view'),
    url(r'^logout/$',demo.views.logout,name='logout'),
    url(r'^loggedin/$',demo.views.loggedin,name='loggedin'),
    url(r'^register/$',demo.views.register_user,name='register_user'),
    url(r'^success/$', demo.views.success, name='success'),
]
