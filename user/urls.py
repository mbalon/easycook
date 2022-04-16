from django.urls import path

from .views import ProfileCreateView, ProfileDetailView

urlpatterns = [
    path("new-profile/", ProfileCreateView.as_view(), name="profile_create"),
    path("profile-view", ProfileDetailView.as_view(), name="profile_detail")
]