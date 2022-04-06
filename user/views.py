from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    fields = ['name', 'biography']


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
    model = Profile
    fields = ['name', 'biography']


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = 'base.html'

