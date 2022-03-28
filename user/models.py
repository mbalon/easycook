from django.db.models import CASCADE, Model, OneToOneField, TextField
from django.contrib.auth.models import User


class Profile(Model):
    """ This class is used to create accounts on site"""
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(null=True)