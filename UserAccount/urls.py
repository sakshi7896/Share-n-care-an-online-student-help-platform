from django.conf.urls import include,url
from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from . import views
urlpatterns = [
    url(r'^login',login, {'template_name': 'UserAccount/login.html'}),
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^register',views.register,name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^write-to-us/$', views.writetous, name='writetous'),
    url(r'^logout/',logout,{'template_name': 'UserAccount/logout.html'}),

]
