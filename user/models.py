from django.db.models import CASCADE, Model, OneToOneField, TextField, ForeignKey
from django.contrib.auth.models import User

from easycook.recipe.models import Recipe

class Profile(Model):
    """ This class is used to create accounts on site"""
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(null=True)


class Comment(Model):
    user = ForeignKey(Profile)
    recipe = ForeignKey(Recipe)
    content = TextField()
