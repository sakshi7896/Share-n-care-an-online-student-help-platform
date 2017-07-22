from django.conf.urls import include,url
from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from . import views


urlpatterns = [
   
    url(r'^register',views.register,name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^write-to-us/$', views.writetous, name='writetous'),
    url(r'^logout/',logout,{'template_name': 'UserAccount/login.html'}, name='logout'),
    url(r'^search/',views.search_view, name='search_view'),
    url(r'^search_book/',views.search_book, name='search_book'),
    url(r'^book_form/$', views.new_book_post, name='book_form'),
	url(r'^donate_book_form/$', views.donate_book_post, name='donate_book_form'),
	url(r'^counselling_form/$', views.counselling_post, name='counselling_form'),
    url(r'^home/$', views.home, name='home'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^view_profile/$', views.view_profile, name='view_profile'),



]


