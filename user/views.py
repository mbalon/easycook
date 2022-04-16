from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from logging import getLogger


from models import Profile
from forms import SignUpForm, ProfileForm


LOGGER = getLogger()


class ProfileCreateView(CreateView):
    template_name = "new_profile.html"
    form_class = SignUpForm

    def form_invalid(self, form):
        LOGGER.warning("Użytkownik przesłał nieprawidłowe dane")
        return super().form_invalid(form)


class ProfileDetailView(DetailView):
    template_name = "profile.html"
    model = Profile

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Profile.objects.filter(user=self.request.user).exists():
            profile = Profile.objects.get(user=self.request.user)
            context["biography"] = profile.biography
        return context


class ProfileUpdateView(UpdateView):
    template_name = "form.html"
    form_class = ProfileForm
    success_url = reverse_lazy("profile")
    model = User

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = 'base.html'


class SubmittableLoginView(LoginView):
    template_name = "login.html"


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = "form.html"
    success_url = reverse_lazy("home")

