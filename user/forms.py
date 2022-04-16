from django.contrib.auth.forms import (
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.forms import CharField, Textarea, ModelForm

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "first_name", "last_name"]

    biography = CharField(
        label="Tell us Your Story", widget=Textarea, min_length=40, required=False
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        biography = self.cleaned_data["biography"]
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return super().save(commit)


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

    biography = CharField(
        label="Tell us Your Story", widget=Textarea, min_length=40, required=False
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        result = super().save(commit)
        biography = self.cleaned_data["biography"]
        profile = Profile.objects.filter(user=result).exists()
        if not profile:
            profile = Profile(user=result, biography=biography)
        else:
            profile = Profile.objects.get(user=result)
            profile.biography = biography
        if commit:
            profile.save()
        return result
