from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

app_name = "tracker"

urlpatterns = [
    # default homepage (index site)

    # /tracker
    url(r'^$', views.index, name='index'),

    # /tracker/home
    url(r'^home/$', views.index, name='home'),

    # /tracker/register
    url(r'^register/$', views.RegisterUserFormView.as_view(), name='register'),

    # /tracker/login
    url(r'^login/$', views.LoginUserFormView.as_view(), name='login'),

    # /tracker/logout
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    # /tracker/app
    url(r'^app/$', views.TrackListView.as_view(), name='tracker_app'),

    # /tracker/app/decs/<id>
    url(r'^app/decs/(?P<track_id>[0-9]+)$', views.decrementSeason, name='dec_season'),

    # /tracker/app/incs/<id>
    url(r'^app/incs/(?P<track_id>[0-9]+)$', views.incrementSeason, name='inc_season'),

    # /tracker/app/dece/<id>
    url(r'^app/dece/(?P<track_id>[0-9]+)$', views.decrementEpisode, name='dec_episode'),

    # /tracker/app/ince/<id>
    url(r'^app/ince/(?P<track_id>[0-9]+)$', views.incrementEpisode, name='inc_episode'),

    # /tracker/app/add/
    url(r'^app/add_track/$', views.CreateNewTrackFormView.as_view(), name='add_track'),

    # /tracker/app/edit/<id>
    url(r'^app/edit/(?P<track_id>[0-9]+)$', views.editTrack, name='edit_track'),

]
