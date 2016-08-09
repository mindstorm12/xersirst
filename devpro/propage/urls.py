from django.conf.urls import url

from . import views

app_name = 'propage'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^ivi/$', views.IviView, name='ivi'),
    url(r'^ivi/about/$', views.About, name='about'),
    url(r'^ivi/game_rab/$', views.Game_rab, name='game_rab'),


]