from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view()),
	url(r'^logout/$', auth_views.LogoutView.as_view()),
	url(r'^$', views.index, name='index'),
	url(r'^(?P<person_id>[0-9]+)$', views.details, name='details'),
	url(r'^addperson$', views.add_person, name='add_person'),
	url(r'^person/(?P<person_id>[0-9]+)/delete$', views.delete_person, name='delete_person')
]