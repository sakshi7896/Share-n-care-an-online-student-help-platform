from django.conf.urls import include,url
from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    url(r'^register',views.register,name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^write-to-us/$', views.writetous, name='writetous'),
    url(r'^logout/',logout,{'template_name': 'UserAccount/login.html'}, name='logout'),
    url(r'^search/',views.search_view, name='search_view'),
    url(r'^search_book/',views.search_book, name='search_book'),
    url(r'^book_form/$', views.new_book_post, name='book_form'),
    url(r'^home/$', views.home, name='home'),
    
    



]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

