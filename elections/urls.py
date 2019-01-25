from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'elections'
urlpatterns = [
	path('', views.index, name = 'home'),
	#path('areas/<str:area>[가-힣]/',views.areas),
	#path('areas/<str:area>[가-힣]/results',views.results),
	url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
	url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
	path('polls/<int:poll_id>/',views.polls),
	url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates),
]