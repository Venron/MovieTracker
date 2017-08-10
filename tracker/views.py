from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View, UpdateView, DeleteView, CreateView
from django.views import generic
from .forms import UserForm, UserLoginForm, TrackForm
from django.contrib.auth import authenticate, login, logout
from django.http import *
from .models import Track
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from datetime import datetime


class IndexView(View):
    template_name = "tracker/base.html"

    def get(self, request):
        return HttpResponse("<h1>Index</h1>")


'''
    Methods e.g. login
'''


def index(request):
    return render(request, "tracker/index.html")


@login_required(login_url="tracker:login")
def decrementSeason(request, track_id):
    my_track = Track.objects.get(id=track_id)
    season = my_track.season
    new_season = season - 1
    # no ability to start at season 0. season 1 is the first season
    if new_season < 1:
        # don't perform any updates
        messages.info(request, "You are already on the first season!")
        return redirect("tracker:tracker_app")

    my_track.season = new_season
    my_track.save()
    messages.info(request, "Updated: " + my_track.title)
    return redirect("tracker:tracker_app")


@login_required(login_url="tracker:login")
def incrementSeason(request, track_id):
    my_track = Track.objects.get(id=track_id)
    season = my_track.season
    new_season = season + 1
    if new_season > 100:
        messages.info(request, "Maximum limit of 100 seasons reached!")
        return redirect("tracker:tracker_app")
    my_track.season = new_season
    my_track.save()
    messages.info(request, "Updated: " + my_track.title)
    return redirect("tracker:tracker_app")


@login_required(login_url="tracker:login")
def decrementEpisode(request, track_id):
    my_track = Track.objects.get(id=track_id)
    episode = my_track.episode
    new_episode = episode - 1
    # no ability to start at episode 0. episode 1 is the first episode
    if new_episode < 1:
        # don't perform any updates
        messages.info(request, "You are already on the first episode!")
        return redirect("tracker:tracker_app")

    my_track.episode = new_episode
    my_track.save()
    messages.info(request, "Updated: " + my_track.title)
    return redirect("tracker:tracker_app")


@login_required(login_url="tracker:login")
def incrementEpisode(request, track_id):
    my_track = Track.objects.get(id=track_id)
    episode = my_track.episode
    new_episode = episode + 1
    if new_episode > 2500:
        messages.info(request, "Maximum limit of 2500 episodes reached!")
        return redirect("tracker:tracker_app")
    my_track.episode = new_episode
    my_track.save()
    messages.info(request, "Updated: " + my_track.title)
    return redirect("tracker:tracker_app")


@login_required(login_url="tracker:login")
def editTrack(request, track_id):
    return redirect("tracker:index")


'''
    Classes e.g. ModelViews
'''


class RegisterUserFormView(View):
    form_class = UserForm
    template_name = "tracker/register_form.html"

    username = ""

    # First access to page
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    # Submit of registration form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # do not save to the DB yet

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            #return redirect("tracker:index")
            return render(request, "tracker/registration_success.html", {"form": form, "username": username})
        return render(request, self.template_name, {"form": form})




class LoginUserFormView(View):
    form_class = UserLoginForm
    template_name = "tracker/login_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        # debug
        if form.is_valid():
            print("form is valid")
        else:
            print("form.errors: " + str(form.errors))
            print("form.non_field_errors: " + str(form.non_field_errors))
            print("form is not valid")

        if form.is_valid():
            # return redirect("http://google.de")
            # user = form.save(commit=False)

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # use special password to set the hashed password (plaintext comparison is unsafe)
            # user.set_password(password)

            # authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                # if user.is_active:
                #     login(request, user)

                return redirect("tracker:index")
            return render(request, self.template_name,
                          {"form": form, "login_error": "Username and password did not match."})
        else:
            # return redirect("http://bing.com")
            return render(request, self.template_name, {"form": form})


class TrackListView(LoginRequiredMixin, generic.ListView):
    login_url = "tracker:login"
    template_name = "tracker/tracker_view.html"
    context_object_name = "all_tracks"

    def get_queryset(self):
        username = self.request.user.username
        return Track.objects.filter(user__username=username).order_by('title')


class CreateNewTrackFormView(View):
    form_class = TrackForm
    template_name = "tracker/add_new_track.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            track = form.save(commit=False)
            track.user = request.user
            track.started = datetime.now()
            track.save()
            return redirect("tracker:tracker_app")
        else:
            return render(request, self.template_name,
                          {"form": form, "add_error": "Sorry! We could not add your track. Please try again later."})


class EditExistingTrack(UpdateView):
    model = Track
    form_class = TrackForm
    template_name = "tracker/edit_track.html"
    # fields = ["title", "season", "episode"]
    success_url = reverse_lazy("tracker:tracker_app")

class DeleteExistingTrack(DeleteView):
    model = Track
    success_url = reverse_lazy("tracker:tracker_app")