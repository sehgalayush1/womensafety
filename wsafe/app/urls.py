from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_view, name='login'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^signup$', views.signup, name='signup'),
	url(r'^dashboard$', views.dashboard, name='dashboard'),
]